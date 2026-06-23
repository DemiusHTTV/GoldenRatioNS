import FiCalculationDegree
from Logos import GoldenNumber

class Normalization:
    ''' класс для нормализациии ответа при 11 22 и тд'''
    
    def __init__(self, a:GoldenNumber,b:GoldenNumber)-> None: 
       self.a = self.normalize(a)
       self.b = self.normalize(b)

    def normalize(n:GoldenNumber) -> GoldenNumber:
        digits=[0]*20
        digits[0]=int(n)
        changed =True
        while(changed):
            for i in digits:
                if digits[i]>=2:
                    count=digits[i]//2
                    digits%=2
                    digits[n+1]+=count
                    digits[n-2]+=count
                    changed =True

            for j in digits:
                if digits[j] ==1 and digits[j-1]==1:
                    digits[j+1] = digits[j]     



            
        