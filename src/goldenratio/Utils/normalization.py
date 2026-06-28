from fractions import Fraction
from goldenratio.Logos import GoldenNumber
from goldenratio.Utils.fi_degree import FiCalculationDegree
from goldenratio.Utils.fi_base import PhiBase


class Normalization:
    """Нормализация GoldenNumber в базе phi."""

    def __init__(self, result: GoldenNumber) -> None:
        digits = PhiBase.to_digits(result)
        self.phi = PhiBase(self.normalize(digits))

    def __str__(self) -> str:
        return str(self.phi)

    def __int__(self) -> int:
        calc = FiCalculationDegree()
        result = GoldenNumber(Fraction(0), Fraction(0))
        for k in self.phi.digits:
            result = result + calc.fi_degree(k)
        return int(result)

    @staticmethod
    def normalize(digits: dict) -> dict:
        if not digits:
            return {}

        min_degree = min(digits.keys())
        max_degree = max(digits.keys())

        for k in range(min_degree - 2, max_degree + 3):
            if k not in digits:
                digits[k] = 0

        changed = True
        while changed:
            changed = False

            sorted_keys = sorted(digits.keys())
            for i in range(len(sorted_keys) - 2):
                k = sorted_keys[i]
                if digits.get(k, 0) >= 1 and digits.get(k + 1, 0) >= 1:
                    digits[k] -= 1
                    digits[k + 1] -= 1
                    digits[k + 2] = digits.get(k + 2, 0) + 1
                    changed = True
                    break

            sorted_keys_desc = sorted(digits.keys(), reverse=True)
            for k in sorted_keys_desc:
                if digits.get(k, 0) >= 2:
                    count = digits[k] // 2
                    digits[k] -= count * 2
                    digits[k + 1] = digits.get(k + 1, 0) + count
                    digits[k - 2] = digits.get(k - 2, 0) + count
                    changed = True
                    break

        return {k: v for k, v in digits.items() if v != 0}
