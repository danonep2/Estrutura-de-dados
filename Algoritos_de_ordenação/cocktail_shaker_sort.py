def cocktailShakeShort (l): 
    indexL = 0
    indexR = len(l)
    while indexL < indexR:
        for i in range(indexL, indexR-1):
            if l[i] > l[i+1]:
                l[i+1],l[i] = l[i],l[i+1]
        indexR -= 1
        for i in range(indexR -1,indexL,-1):
            if l[i] < l[i-1]:
                l[i-1],l[i] = l[i],l[i-1]
        indexL += 1
    return l
