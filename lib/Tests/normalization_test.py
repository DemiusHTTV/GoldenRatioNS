import pytest
from fractions import Fraction
from goldenratio.Utils.normalization import Normalization
from goldenratio.Logos import GoldenNumber


def test_normalize_empty_dict():
    result = Normalization.normalize({})
    assert result == {}

def test_normalize_number():
    n = GoldenNumber(11, 0)
    m = GoldenNumber(4, 0)
    assert Normalization(n).phi.digits == {4: 1, 2: 1, 0: 1, -2: 1, -4: 1}
    assert Normalization(m).phi.digits == {2: 1, 0: 1, -2: 1}

def test_already_normalized():
    result = Normalization.normalize({5: 1})
    assert result == {5: 1}

# φ⁻¹ + φ⁻² = φ⁰
def test_normalize_fractional_adjacent():
    assert Normalization.normalize({-1: 1, -2: 1}) == {0: 1}

# 2·φ⁻¹ = φ⁰ + φ⁻³
def test_normalize_fractional_duplicate():
    assert Normalization.normalize({-1: 2}) == {0: 1, -3: 1}

def test_int_method():
    assert int(Normalization(GoldenNumber(11, 0))) == 11
    assert int(Normalization(GoldenNumber(4, 0))) == 4
