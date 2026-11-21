import math

def light_samples(size, distance):
    """光源采样数。"""
    raise NotImplementedError("TODO: light_samples")

def temporal_weight(motion, base):
    """时域权重。"""
    raise NotImplementedError("TODO: temporal_weight")

def spatial_radius(world, scale):
    """空间核半径。"""
    raise NotImplementedError("TODO: spatial_radius")

def depth_reject(prev, cur, threshold):
    """深度拒绝。"""
    raise NotImplementedError("TODO: depth_reject")

def alpha_opacity(alpha, cutoff):
    """alpha 镂空。"""
    raise NotImplementedError("TODO: alpha_opacity")

def transmission(alpha):
    """透明透射率。"""
    raise NotImplementedError("TODO: transmission")

def contact_weight(distance):
    """接触硬化。"""
    raise NotImplementedError("TODO: contact_weight")

def reset_on_move(moved):
    """光源移动重置。"""
    raise NotImplementedError("TODO: reset_on_move")

def combined(a, b):
    """多光源叠加。"""
    raise NotImplementedError("TODO: combined")

def penumbra(size, distance):
    """半影尺寸。"""
    raise NotImplementedError("TODO: penumbra")

def shadow_key(light, index):
    """阴影键。"""
    raise NotImplementedError("TODO: shadow_key")

def reproject(uv, motion):
    """重投影。"""
    raise NotImplementedError("TODO: reproject")

def noise_seed(frame):
    """噪声种子。"""
    raise NotImplementedError("TODO: noise_seed")

def valid_uv(uv):
    """UV 合法性。"""
    raise NotImplementedError("TODO: valid_uv")

def shadow_id(seed, index):
    """阴影 id。"""
    raise NotImplementedError("TODO: shadow_id")
