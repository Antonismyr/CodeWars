import numpy as np
def persistence(n):
    count = 0
    numbers = [int(i) for i in str(n)]
    while len(numbers)>1:
        count +=1
        res = np.prod(numbers)
        numbers = [int(i) for i in str(res)]
    return count