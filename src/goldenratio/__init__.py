from Logos.golden_number import GoldenNumber
  
 
def normalize(value: GoldenNumber):
     from Utils.normalization import Normalization 
     return Normalization(value)

def fi_degree(n: int) -> GoldenNumber:
    from Utils.fi_degree import FiCalculationDegree
    return FiCalculationDegree().fi_degree(n)