from goldenratio.Utils.fi_base import PhiBase
from goldenratio.Utils.normalization import Normalization

class PhiArithmetic:
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
        pass
