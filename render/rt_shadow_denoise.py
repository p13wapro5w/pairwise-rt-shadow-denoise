import math

# 光源采样数的硬上限，避免面光贴近表面时采样爆炸。
MAX_LIGHT_SAMPLES = 64


def light_samples(size, distance):
    """光源采样数。

    按光源对当前着色点的张角采样：光源越大、距离越近，需要的采样
    越多；太阳这类远处光源张角很小，退化为单根光线。面光因此会自
    动获得多采样，而不是和太阳一样只投出一条硬边。
    """
    size = abs(float(size))
    distance = abs(float(distance))
    if distance <= 0.0:
        return 1
    samples = int(math.ceil(size / distance))
    return max(1, min(samples, MAX_LIGHT_SAMPLES))


def temporal_weight(motion, base):
    """时域累积权重（运动自适应）。

    运动越大，历史帧越不可信，权重按 1/(1+motion) 衰减，避免移动
    物体后拖出阴影尾巴；静止时保持基础权重。
    """
    motion = abs(float(motion))
    base = min(max(float(base), 0.0), 1.0)
    return base / (1.0 + motion)


def spatial_radius(world, scale):
    """空间降噪核半径。

    由世界尺度换算到像素：world 是核在世界空间的半径，scale 是每
    世界单位对应的像素数。近处核变大、远处核变小，避免近处被抹平
    而远处仍然噪。
    """
    return abs(float(world)) * abs(float(scale))


def depth_reject(prev, cur, threshold):
    """深度不连续检测。

    返回 True 表示前后帧深度可视为连续、允许复用历史；超过阈值则
    拒绝，防止角色脚底和地面阴影粘在一起。
    """
    threshold = abs(float(threshold))
    return abs(float(prev) - float(cur)) <= threshold


def alpha_opacity(alpha, cutoff):
    """alpha 测试后的不透明度。

    低于裁剪阈值的碎片完全不遮挡（保留树叶镂空），高于阈值则视为
    不透明，而不是把整片叶子写成实心板。
    """
    alpha = float(alpha)
    cutoff = float(cutoff)
    return 1.0 if alpha >= cutoff else 0.0


def transmission(alpha):
    """透明物体的透射率。

    透明物体按 1 - 不透明度投影阴影，让玻璃后方保留部分光照，而不
    是完全无遮挡。
    """
    return min(max(1.0 - float(alpha), 0.0), 1.0)


def contact_weight(distance):
    """接触硬化权重。

    距离越贴近地面，权重越高（接触处阴影更实），随距离以 1/(1+d)
    平滑衰减。
    """
    distance = max(float(distance), 0.0)
    return 1.0 / (1.0 + distance)


def reset_on_move(moved):
    """光源移动时是否重置历史累积。

    光源发生移动后必须丢弃上一帧历史，否则阴影追不上太阳。
    """
    return bool(moved)


def combined(a, b):
    """多光源联合降噪。

    多个光源的遮挡应取并集，而不是各自降噪后相加；取较小值可避免
    接缝处出现双重暗边。
    """
    return min(a, b)


def penumbra(size, distance):
    """半影尺寸（角尺寸）。

    光源尺寸相对距离的张角；张角越大，半影越宽、边缘越软。
    """
    size = abs(float(size))
    distance = abs(float(distance))
    if distance <= 0.0:
        return 0.0
    return size / distance


def shadow_key(light, index):
    """阴影缓存键。"""
    return f"{light}:{index}"


def reproject(uv, motion):
    """把当前帧 UV 按运动向量投影回上一帧。"""
    u, v = uv
    du, dv = motion
    return (u - du, v - dv)


def noise_seed(frame):
    """噪声种子：每帧一个确定且可复现的种子。"""
    return int(frame)


def valid_uv(uv):
    """UV 是否落在 [0, 1] 屏幕范围内。"""
    u, v = uv
    return 0.0 <= float(u) <= 1.0 and 0.0 <= float(v) <= 1.0


def shadow_id(seed, index):
    """阴影样本 id。"""
    return f"{seed}:{index}"
