from fractions import Fraction
from goldenratio.Logos import GoldenNumber
from goldenratio.Utils.fi_degree import FiCalculationDegree
from goldenratio.Utils.fi_base import PhiBase
from goldenratio.Utils.normalization import Normalization

class PhiBase:
    """Представление числа в фи-системе счисления."""

    def __init__(self, digits: dict[int, int]) -> None:
        self.digits = digits

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
    
    @staticmethod
    def add(a:PhiBase,b:PhiBase)->PhiBase:
        merged:dict[int,int]=dict(a.digits)
        for k,v in b.digits.items():
            if k in merged:
                merged[k]=merged[k]+v
            else:
                merged[k]=v
        return PhiBase(Normalization.normalize(merged))
    
    @staticmethod
    def sub(a:PhiBase,b:PhiBase)->PhiBase:
        merged:dict[int,int]=dict(a.digits)
        for k,v in b.digits.items():
            if k in merged:
                merged[k]=merged[k]-v
            else:
                merged[k]=v
        return PhiBase(Normalization.normalize(merged))
    
    @staticmethod
    def mul(a:PhiBase,b:PhiBase)->PhiBase:
        merged:dict[int,int]={}
        for deg_a,coef_a in a.digits:
            for deg_b,coef_b in b.digits:
                new_deg=deg_a+deg_b
                if new_deg in merged:
                    merged[new_deg]=merged[new_deg]+coef_a*coef_b
                else:
                    merged[new_deg]=coef_a*coef_b
        return PhiBase(Normalization.normalize(merged))
    

