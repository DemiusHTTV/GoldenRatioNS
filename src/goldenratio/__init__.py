from goldenratio.Logos.golden_number import GoldenNumber

 
def normalize(value: GoldenNumber):
     from goldenratio.Utils.normalization import Normalization 
     return Normalization(value)

def fi_degree(n: int) -> GoldenNumber:
    from goldenratio.Utils.fi_degree import FiCalculationDegree
    return FiCalculationDegree().fi_degree(n)

def translate_to_fi(value:GoldenNumber):
     from goldenratio.Utils.fi_base import PhiBase
     return PhiBase.from_golden_number(value)