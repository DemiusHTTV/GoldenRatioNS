from fractions import Fraction


class GoldenNumber:
    def __init__(self,a:Fraction,b:Fraction)-> None:
        self.a=a
        self.b=b

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

    

      
