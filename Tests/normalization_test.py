import pytest
from fractions import Fraction
from Normalization import Normalization
from Logos import GoldenNumber


def test_normalize_empty_dict():
    result = Normalization.normalize({})
    assert result == {}

