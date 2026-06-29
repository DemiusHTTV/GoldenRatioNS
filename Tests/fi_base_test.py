from fractions import Fraction
from goldenratio.Utils.fi_base import PhiBase
from goldenratio.Logos import GoldenNumber


def test_str_eleven():
    digits = {4: 1, 2: 1, 0: 1, -2: 1, -4: 1}
    assert str(PhiBase(digits)) == "10101.0101"

def test_str_four():
    digits = {2: 1, 0: 1, -2: 1}
    assert str(PhiBase(digits)) == "101.01"

def test_str_one():
    digits = {0: 1}
    assert str(PhiBase(digits)) == "1"

def test_str_empty():
    assert str(PhiBase({})) == "0"

def test_to_digits_eleven():
    n = GoldenNumber(11, 0)
    result = PhiBase.to_digits(n)
    assert result == {4: 1, 2: 1, 0: 1, -2: 1, -4: 1}

def test_to_digits_four():
    n = GoldenNumber(4, 0)
    result = PhiBase.to_digits(n)
    assert result == {2: 1, 0: 1, -2: 1}

def test_to_digits_1984():
    n = GoldenNumber(1984, 0)
    result = PhiBase.to_digits(n)
    assert str(PhiBase(result)) == "1010001001001000.1001001000100001"