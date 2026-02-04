import numpy as np 
from fairsharer.fairsharer import fair_sharer

def test_fair_sharer():
    result_1 = fair_sharer([0, 1000, 800, 0], 1)
    assert result_1 == [100.0, 800.0, 900.0, 0.0]

    result_2 = fair_sharer([0, 1000, 800, 0], 2)
    assert result_2 == [100.0, 890.0, 720.0, 90.0]