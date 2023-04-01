def legit(i):
    num = list(map(int, str(i)))
    fin = sum([i**(k+1) for k, i in enumerate(num)])
    return i == fin
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    return [i for i in range(a, b+1) if legit(i)]