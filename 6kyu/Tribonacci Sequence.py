def tribonacci(signature, n):
    sol = [] 
    for i in range(n):
        if i<len(signature):
            sol.append(signature[i])
        else:
            sol.append(sum(sol[i-3:i]))
    return sol