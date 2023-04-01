import numpy as np 
def delete_nth(order,max_e):
    orderNp = np.array(order)
    return [k for i, k in enumerate(orderNp) if sum(orderNp[:i+1] == k) <= max_e] 