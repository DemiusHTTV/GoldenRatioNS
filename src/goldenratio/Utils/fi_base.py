from fractions import Fraction
from goldenratio.Logos import GoldenNumber
from goldenratio.Utils.fi_degree import FiCalculationDegree
from goldenratio.Utils.normalization import Normalization


class PhiBase:
    """Представление числа в фи-системе счисления."""

    def __init__(self, digits: dict[int, int]) -> None:
        self.digits = digits

    @classmethod
    def from_golden_number(cls, value: GoldenNumber) -> "PhiBase":
        return cls(Normalization.normalize(cls.to_digits(value)))

    def __str__(self) -> str:
        if not self.digits:
            return "0"
        max_k = max(self.digits.keys())
        min_k = min(self.digits.keys())
        bits = []
        for k in range(max_k, min_k - 1, -1):
            if k == -1:
                bits.append(".")
            bits.append(str(self.digits.get(k, 0)))
        return "".join(bits)

    def __int__(self) -> int:
        calc = FiCalculationDegree()
        result = GoldenNumber(Fraction(0), Fraction(0))
        for k in self.digits:
            result = result + calc.fi_degree(k)
        return int(result)

    def __eq__(self, other: "PhiBase") -> bool:
        return self.digits == other.digits

    @staticmethod
    def to_digits(value: GoldenNumber) -> dict:
        """Жадный перевод GoldenNumber в цифры базы phi."""
        digits = {}
        remainder = value
        zero = GoldenNumber(Fraction(0), Fraction(0))
        calc = FiCalculationDegree()
        K_TOP = calc.max_degree(int(value)) + 1
        K_BOTTOM = -K_TOP
        for k in range(K_TOP, K_BOTTOM - 1, -1):
            if remainder == zero:
                break
            phi_k = calc.fi_degree(k)
            if not phi_k.less_or_equal(zero) and not remainder.is_less(phi_k):
                digits[k] = 1
                remainder = remainder - phi_k
        return digits

    def __add__(self, other: "PhiBase") -> "PhiBase":
        merged: dict[int, int] = dict(self.digits)
        for k, v in other.digits.items():
            merged[k] = merged.get(k, 0) + v
        return PhiBase(Normalization.normalize(merged))

    def __sub__(self, other: "PhiBase") -> "PhiBase":
        merged: dict[int, int] = dict(self.digits)
        for k, v in other.digits.items():
            merged[k] = merged.get(k, 0) - v
        return PhiBase(Normalization.normalize(merged))

    def __mul__(self, other: "PhiBase") -> "PhiBase":
        merged: dict[int, int] = {}
        for deg_a, coef_a in self.digits.items():
            for deg_b, coef_b in other.digits.items():
                new_deg = deg_a + deg_b
                merged[new_deg] = merged.get(new_deg, 0) + coef_a * coef_b
        return PhiBase(Normalization.normalize(merged))
