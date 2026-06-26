import pytest
from fractions import Fraction
from Logos.golden_number import GoldenNumber


def test_str():
    x = GoldenNumber(Fraction(1), Fraction(2))
    assert str(x) == "1 + 2·√5"

def test_add():
    x = GoldenNumber(Fraction(1), Fraction(2))
    y = GoldenNumber(Fraction(3), Fraction(1))
    result = x + y
    assert result == GoldenNumber(Fraction(4), Fraction(3))

def test_sub():
    x = GoldenNumber(Fraction(3), Fraction(2))
    y = GoldenNumber(Fraction(1), Fraction(1))
    result = x - y
    assert result == GoldenNumber(Fraction(2), Fraction(1))

#с отриц результатом
def test_sub_negative():
    x = GoldenNumber(Fraction(1), Fraction(0))
    y = GoldenNumber(Fraction(3), Fraction(0))
    result = x - y
    assert result == GoldenNumber(Fraction(-2), Fraction(0))

def test_mul():
    x = GoldenNumber(Fraction(1), Fraction(2))
    y = GoldenNumber(Fraction(3), Fraction(1))
    result = x * y
    assert result == GoldenNumber(Fraction(13), Fraction(7))

#на 0
def test_mul_zero():
    x = GoldenNumber(Fraction(1), Fraction(2))
    y = GoldenNumber(Fraction(0), Fraction(0))
    result = x * y
    assert result == GoldenNumber(Fraction(0), Fraction(0))

#целое число
def test_is_int_true():
    x = GoldenNumber(Fraction(5), Fraction(0))
    assert x.is_int()

#коэф b не равен 0
def test_is_int_false():
    x = GoldenNumber(Fraction(5), Fraction(1))
    assert not x.is_int()

#a дробь
def test_is_int_fraction():
    x = GoldenNumber(Fraction(5, 2), Fraction(0))
    assert not x.is_int()

def test_int():
    x = GoldenNumber(Fraction(7), Fraction(0))
    assert int(x) == 7

#не целое
def test_int_raises():
    x = GoldenNumber(Fraction(1), Fraction(2))
    with pytest.raises(ValueError):
        int(x)

def test_eq_true():
    x = GoldenNumber(Fraction(1), Fraction(2))
    y = GoldenNumber(Fraction(1), Fraction(2))
    assert x == y

def test_eq_false():
    x = GoldenNumber(Fraction(1), Fraction(2))
    y = GoldenNumber(Fraction(1), Fraction(3))
    assert not (x == y)

def test_le_true():
    x = GoldenNumber(Fraction(1), Fraction(0))
    y = GoldenNumber(Fraction(2), Fraction(0))
    assert x <= y

def test_le_false():
    x = GoldenNumber(Fraction(3), Fraction(0))
    y = GoldenNumber(Fraction(1), Fraction(0))
    assert not (x <= y)

def test_le_equal():
    x = GoldenNumber(Fraction(2), Fraction(0))
    y = GoldenNumber(Fraction(2), Fraction(0))
    assert x <= y

# отриц и полож
def test_le_neg_pos():
    x = GoldenNumber(Fraction(-1), Fraction(0))
    y = GoldenNumber(Fraction(1), Fraction(0))
    assert x <= y

#отриц и полож
def test_le_pos_neg():
    x = GoldenNumber(Fraction(1), Fraction(0))
    y = GoldenNumber(Fraction(-1), Fraction(0))
    assert not (x <= y)

# иррац меньше целого
def test_le_irrational_true():
    x = GoldenNumber(Fraction(0), Fraction(1))
    y = GoldenNumber(Fraction(3), Fraction(0))
    assert x <= y

# целое больше иррац
def test_le_irrational_false():
    x = GoldenNumber(Fraction(3), Fraction(0))
    y = GoldenNumber(Fraction(0), Fraction(1))
    assert not (x <= y)

#оба иррац
def test_complex_comparison():
    x = GoldenNumber(Fraction(1), Fraction(1))
    y = GoldenNumber(Fraction(2), Fraction(1, 2))
    assert not (x <= y)

def test_lt_true():
    x = GoldenNumber(Fraction(1), Fraction(0))
    y = GoldenNumber(Fraction(3), Fraction(0))
    assert x < y

def test_lt_false():
    x = GoldenNumber(Fraction(3), Fraction(0))
    y = GoldenNumber(Fraction(1), Fraction(0))
    assert not (x < y)

# иррац меньше целого
def test_lt_irrational_true():
    x = GoldenNumber(Fraction(0), Fraction(1))
    y = GoldenNumber(Fraction(3), Fraction(0))
    assert x < y

#целое больше иррац
def test_lt_irrational_false():
    x = GoldenNumber(Fraction(3), Fraction(0))
    y = GoldenNumber(Fraction(0), Fraction(1))
    assert not (x < y)