from fractions import Fraction

class GoldenNumber:
    def __init__(self,a:int,b:int)-> None:
        self.a=Fraction(a)
        self.b=Fraction(b)

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
    
    def __int__(self)->int: 
        if self.is_int():
            return int(self.a)
        else:
            raise ValueError("Cannot convert to int")
    
    def is_equally(self,other:"GoldenNumber")->bool:
        return self.a==other.a and self.b==other.b
    
    def less_or_equal(self,other:"GoldenNumber")->bool:
        x=self.a-other.a
        y=self.b-other.b

        if y>=0:
            if x>=0: return False
            else:
                return (x**2) >= (5 * (y**2))
        else:
            if x<0: return True
            else:
                return (x**2) <= (5 * (y**2))
    
    def is_less(self,other:"GoldenNumber")->bool:
        return self.less_or_equal(other) and not self.is_equally(other)

    def __eq__(self, other): 
        return self.is_equally(other)
    

    def __le__(self, other): 
        return self.less_or_equal(other)
    

    def __lt__(self, other): return self.is_less(other)


   