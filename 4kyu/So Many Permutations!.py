import itertools
def permutations(s):
    perm_set = list(set(itertools.permutations(s)))
    return [''.join(i) for i in perm_set]