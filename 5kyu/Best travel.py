from itertools import combinations
import numpy as np 
def choose_best_sum(t, k, ls):
    dist = np.array([sum(i) for i in list(combinations(ls,k))])
    distdiff = t-dist
    return dist[distdiff>=0][np.argmin(distdiff[distdiff>=0])] if len(distdiff[distdiff>=0]) else None