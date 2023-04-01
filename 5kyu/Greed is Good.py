import numpy as np 
def score(dice):
    diceNp = np.array(dice)
    score = 0 
    for i in set(dice):
        if sum(i==diceNp) >= 3:
            score+=i*1000 if i == 1 else i*100
            diceNp = np.delete(diceNp, np.where(diceNp==i)[0][:3])
        if i == 1:
            score+=sum(i==diceNp)*100 
        elif i == 5:
            score+=sum(i==diceNp)*50
    return score