from fractions import Fraction
from Logos import GoldenNumber
from Utils.fi_degree import FiCalculationDegree


class Normalization:
    """Нормализация GoldenNumber в базе phi."""

    def __init__(self, result: GoldenNumber) -> None:
          self.digits: dict[int, int] = self.normalize(self.to_digits(result)) 

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

    @staticmethod
    def to_digits(value: GoldenNumber) -> dict:
        """Жадный перевод GoldenNumber в цифры базы phi."""
        digits = {}
        remainder = value
        zero = GoldenNumber(Fraction(0), Fraction(0))

        calc = FiCalculationDegree()
        K_TOP = calc.max_degree(int(value)) + 1
        K_BOTTOM = -64

        for k in range(K_TOP, K_BOTTOM - 1, -1):
            if remainder == zero:
                break
            phi_k = calc.fi_degree(k)
            if not phi_k.less_or_equal(zero) and not remainder.is_less(phi_k):
                digits[k] = 1
                remainder = remainder - phi_k

        return digits
