from decimal import *
def find_nb(m):
    getcontext().prec = 24
    # n^3+(n−1)^3+(n−2)^3+...+1^3 = (n+(n−1)+(n−2)+...+1) ^ 2
    # (n+(n−1)+(n−2)+...+1) = n(n+1)/2
    # (n(n+1)/2)^2 = m
    # n^2 + n - 2 * sqrt(m) = 0
    if 1 ** 2 + 8 * Decimal(m).sqrt() < 0:
        return -1
    else:
        roots = (-1 + Decimal(1 ** 2 + 8 * Decimal(m).sqrt()).sqrt())/2
        return int(roots) if roots == int(roots) else -1