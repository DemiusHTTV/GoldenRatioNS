from Logos import GoldenNumber
from fractions import Fraction
from typing import Literal

class FiCalculationDegree:
  
    def __init__(self):
        self.FI_POS=GoldenNumber(Fraction(1,2),Fraction(1,2))
        self.FI_NEG=GoldenNumber(Fraction(-1,2),Fraction(1,2))
        self.ONE = GoldenNumber(Fraction(1), Fraction(0))

 
    def fi_degree(self,n:int)->GoldenNumber:
        if n == 0:
            return self.ONE
        prev = self.ONE
        if n < 0:
            curr = self.FI_NEG
            for i in range(1, -n):
                temp = curr + prev
                prev = curr
                curr = temp
        else:
            curr = self.FI_POS
            for i in range(2, n + 1):
                temp = curr + prev
                prev = curr
                curr = temp
        return curr
    
    
    def calc_degree(self, val: int, param: Literal["max", "min"]) -> int:
        if val < 0:
            raise ValueError("value must be positive")
        golden_value = GoldenNumber(Fraction(val), Fraction(0))
        n = 0
        if param == "max":
            while self.fi_degree(n + 1) <= golden_value:
                n += 1
            return n
        elif param == "min":
            while self.fi_degree(n - 1) <= golden_value:
                n -= 1
            return n



        