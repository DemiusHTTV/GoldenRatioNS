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