import FiCalculationDegree
from Logos import GoldenNumber

class Normalization:
    ''' класс для нормализациии ответа при 11 2 и тд'''
    
    def __init__(self, a:GoldenNumber,b:GoldenNumber)-> None: 
       self.a = self.normalize(self.to_digits(a))
       self.b = self.normalize(self.to_digits(b))

    
  @staticmethod
    def normalize(digits: dict[int, int]) -> dict[int, int]:
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
                    digits[k - 2] = digits.get(k - 2, 0) + count
                    changed = True
                    break
        digits = {k: v for k, v in digits.items() if v != 0}
        return digits

    @staticmethod
    def to_digits(value: GoldenNumber) -> dict[int, int]:
        """
        Жадный перевод a+b√5 в цифры базы φ. 
        Ключ = степень φ, значение = цифра.
        """
        
        digits: dict[int, int] = {}
        remainder = value                       
        zero = GoldenNumber(Fraction(0), Fraction(0))

        calc = FiCalculationDegree()
        K_TOP = calc.max_degree(value.to_int()) + 1    
        K_BOTTOM = -64    #нижний педел

        for k in range(K_TOP, K_BOTTOM - 1, -1):
            if remainder == zero:
                break
            phi_k = calc.fi_degree(k)

        return dict(digits)