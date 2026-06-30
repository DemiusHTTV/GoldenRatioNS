from fractions import Fraction
from goldenratio.Logos import GoldenNumber
from goldenratio.Utils.fi_degree import FiCalculationDegree


class Normalization:
    """Нормализация GoldenNumber в базе phi."""

    def __init__(self, result: GoldenNumber) -> None:
        from goldenratio.Utils.fi_base import PhiBase  # lazy import — разрывает цикл
        raw_digits = PhiBase.to_digits(result)
        self.phi = PhiBase(self.normalize(raw_digits))

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

            # Правило 1: два соседних 1 → 1 на две позиции выше
            for i in range(len(sorted_keys) - 1):
                k = sorted_keys[i]
                if digits.get(k, 0) >= 1 and digits.get(k + 1, 0) >= 1:
                    digits[k] -= 1
                    digits[k + 1] -= 1
                    digits[k + 2] = digits.get(k + 2, 0) + 1
                    changed = True
                    break

            # Правило 2: дубль (≥2) → раскладывается
            for k in sorted(digits.keys(), reverse=True):
                if digits.get(k, 0) >= 2:
                    count = digits[k] // 2
                    digits[k] -= count * 2
                    digits[k + 1] = digits.get(k + 1, 0) + count
                    digits[k - 2] = digits.get(k - 2, 0) + count
                    changed = True
                    break

            # Правило 3: два соседних -1 → -1 на две позиции выше
            for i in range(len(sorted_keys) - 1):
                k = sorted_keys[i]
                if digits.get(k, 0) <= -1 and digits.get(k + 1, 0) <= -1:
                    digits[k] += 1
                    digits[k + 1] += 1
                    digits[k + 2] = digits.get(k + 2, 0) - 1
                    changed = True
                    break

            # Правило 4: +1 на k+2 и -1 на k → +1 на k+1 (φ^(k+2) - φ^k = φ^(k+1))
            for k in sorted_keys:
                if digits.get(k, 0) <= -1 and digits.get(k + 2, 0) >= 1:
                    digits[k] += 1
                    digits[k + 2] -= 1
                    digits[k + 1] = digits.get(k + 1, 0) + 1
                    changed = True
                    break

        return {k: v for k, v in digits.items() if v != 0}
