from fractions import Fraction


class GoldenNumber:
    def __init__(self,a:Fraction,b:Fraction)-> None:
        self.a=a
        self.b=b

    def __str__(self) -> str:
        return f"{self.a} + {self.b}·√5"

    def __add__(self,other:"GoldenNumber")->"GoldenNumber":
        new_a=self.a+other.a
        new_b=self.b+other.b
        return GoldenNumber(new_a,new_b)

    def __sub__(self,other:"GoldenNumber")->"GoldenNumber":
        new_a=self.a-other.a
        new_b=self.b-other.b
        return GoldenNumber(new_a,new_b)
    
    #(a + b√5) × (c + d√5) = (ac + 5bd) + (ad + bc)√5
    def __mul__(self,other:"GoldenNumber")->"GoldenNumber": 
        new_a=self.a*other.a+5*self.b*other.b
        new_b=self.a*other.b+self.b*other.a
        return GoldenNumber(new_a,new_b)

    def is_int(self)->bool:        
        if self.b==0 and self.a.denominator==1:
            return True
        return False
    
    def to_int(self)->int: 
        if self.is_int():
            return int(self.a)
        else:
            raise ValueError("Cannot convert to int")
        
    
FI_POS=GoldenNumber(Fraction(1,2),Fraction(1,2))
FI_NEG=GoldenNumber(Fraction(-1,2),Fraction(1,2))
ONE = GoldenNumber(Fraction(1), Fraction(0))
def fi_degree(n:int)->GoldenNumber:
    if n == 0:
        return ONE
    prev = ONE
    if n < 0:
        curr = FI_NEG
        for _ in range(1, -n):
            temp = curr + prev
            prev = curr
            curr = temp
    else:
        curr = FI_POS
        for _ in range(2, n + 1):
            temp = curr + prev
            prev = curr
            curr = temp
    return curr