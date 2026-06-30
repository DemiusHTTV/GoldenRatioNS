import pytest
from fractions import Fraction
from goldenratio.Utils.fi_degree import FiCalculationDegree
from goldenratio.Logos import GoldenNumber

calc=FiCalculationDegree()

def test_fi_degree_zero():
    result=calc.fi_degree(0)
    assert result==GoldenNumber(Fraction(1),Fraction(0))

def test_fi_degree_one():
    result=calc.fi_degree(1)
    assert result==GoldenNumber(Fraction(1,2),Fraction(1,2))

def test_fi_degree_two():
    result=calc.fi_degree(2)
    assert result==calc.fi_degree(1)+calc.fi_degree(0)

def test_fi_degree_neg():
    result=calc.fi_degree(-1)
    assert result==GoldenNumber(Fraction(-1,2),Fraction(1,2))

def test_fi_degree_negative_two():
    result = calc.fi_degree(-2)
    assert result == GoldenNumber(Fraction(3, 2), Fraction(-1, 2))

def test_fi_degree_rec():
    for n in range (2,10):
        assert calc.fi_degree(n)==calc.fi_degree(n-1)+calc.fi_degree(n-2)


def test_max_degree_one():
    result=calc.max_degree(1)
    assert result==0

def test_max_degree_two():
    result=calc.max_degree(2)
    assert result==1

def test_max_degree_three():
    result=calc.max_degree(3)
    assert result==2

def test_max_degree_invalid():
    with pytest.raises(ValueError):
        calc.max_degree(-1)