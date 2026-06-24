import FiCalculationDegree
from Logos import GoldenNumber

class Normalization:
    ''' класс для нормализациии ответа при 11 2 и тд'''
    
    def __init__(self, a:GoldenNumber,b:GoldenNumber)-> None: 
       self.a = self.normalize(a)
       self.b = self.normalize(b)

    

    def normalize(digits: list) -> list:

        changed = True
        while changed:
            changed = False

            for i in range(len(digits) - 2):
                if digits[i] == 1 and digits[i+1] == 1:
                    digits[i] = 0
                    digits[i+1] = 0
                    digits[i+2] += 1
                    changed = True
            
            for i in range(len(digits)):
                if digits[i] >= 2:
                    digits[i] -= 2
                    digits[i-2] += 1 
                    changed = True
        return digits