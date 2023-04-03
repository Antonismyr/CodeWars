import numpy as np

def findIds(string, n):
    idx = []
    cycle = 2*n-2
    for i in range(n):
        if i==0 or i==n-1:
            idx.append(np.arange(i, len(string), cycle))
        else:
            idx1 = np.arange(i, len(string), cycle)
            idx2 = np.arange(cycle-i, len(string), cycle)
            idx.append(np.sort(np.concatenate([idx1, idx2])))
    return np.concatenate(idx)

def encode_rail_fence_cipher(string, n):
    stringList = np.array(list(string))
    idx = findIds(string, n)
    return ''.join(list(stringList[idx]))

    
def decode_rail_fence_cipher(string, n):
    stringList = np.array(list(string))
    idx = findIds(string, n)
    decoded = np.empty_like(stringList)
    decoded[idx] = stringList
    return ''.join(list(decoded))