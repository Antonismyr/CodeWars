def is_valid_walk(walk):
    #determine if walk is valid
    startPos = [0, 0]
    if len(walk)!=10:
        return False
    
    dictDir = {'w': 0 , 'e': 0, 'n': 1, 's': 1}
    dictPos = {'w': -1 , 'e': 1, 'n': 1, 's': -1}
    for i in walk:
        startPos[dictDir[i]] +=  dictPos[i]
    if sum([i == 0 for i in startPos]) == 2:
        return True
    else:
        return False