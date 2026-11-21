import pytest
import math
from render import rt_shadow_denoise as mod

CASES = [
    ("samples", 'm.light_samples(2, 1) == 2'),
    ("temporal", 'm.temporal_weight(1, 0.5) == approx(0.25)'),
    ("radius", 'm.spatial_radius(2, 3) == 6'),
    ("reject", 'm.depth_reject(0.5, 0.55, 0.1) is True'),
    ("alpha", 'm.alpha_opacity(0.2, 0.5) == 0.0'),
    ("trans", 'm.transmission(0.5) == approx(0.5)'),
    ("contact", 'm.contact_weight(1) == approx(0.5)'),
    ("reset", 'm.reset_on_move(True) is True'),
    ("comb", 'm.combined(0.3, 0.5) == 0.3'),
    ("pen", 'm.penumbra(2, 4) == approx(0.5)'),
    ("key", 'm.shadow_key("sun", 2) == "sun:2"'),
    ("reproj", 'm.reproject((0.5, 0.5), (0.1, 0.2)) == approx((0.4, 0.3))'),
    ("seed", 'm.noise_seed(7) == 7'),
    ("uv", 'm.valid_uv((0.5, 0.5)) is True'),
    ("id", 'm.shadow_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
