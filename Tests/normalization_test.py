import pytest
from fractions import Fraction
from Utils.normalization import Normalization
from Logos import GoldenNumber


def test_normalize_empty_dict():
    result = Normalization.normalize({})
    assert result == {}

def test_normalize_number():
    n = GoldenNumber(Fraction(11),Fraction(0))
    m = GoldenNumber(Fraction(4), Fraction(0))
    result11 = Normalization(n).digits
    result4 = Normalization(m).digits
    assert result11 == {4: 1, 2: 1, 0: 1, -2: 1, -4: 1}
    assert result4 ==  {2: 1, 0: 1, -2: 1}

def test_already_normalizate():
    result = Normalization.normalize({5:1})
    assert result == {5:1}


# φ⁻¹ + φ⁻² = φ⁰
def test_normalize_fractional_adjacent():
    assert Normalization.normalize({-1: 1, -2: 1}) == {0: 1}


# 2·φ⁻¹ = φ⁰ + φ⁻³ 
def test_normalize_fractional_duplicate():
    assert Normalization.normalize({-1: 2}) == {0: 1, -3: 1}

def test_int_method():
    n = GoldenNumber(Fraction(11),Fraction(0))
    m = GoldenNumber(Fraction(4), Fraction(0))
    result1 = int(Normalization(n))
    result2 = int(Normalization(m))
    assert result1 == 11
    assert result2 == 4