from Logos import GoldenNumber

class FiCalculationDegree:

    FI_POS=GoldenNumber(Fraction(1,2),Fraction(1,2))
    FI_NEG=GoldenNumber(Fraction(-1,2),Fraction(1,2))
    ONE = GoldenNumber(Fraction(1), Fraction(0))

    def fi_degree(n:int)->GoldenNumber:
        if n == 0:
            return ONE
        prev = ONE
        if n < 0:
            curr = FI_NEG
            for i in range(1, -n):
                temp = curr + prev
                prev = curr
                curr = temp
        else:
            curr = FI_POS
            for i in range(2, n + 1):
                temp = curr + prev
                prev = curr
                curr = temp
        return curr
    