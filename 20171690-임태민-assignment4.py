def comb(n,r):
    if r == 0:
        return 1
    elif r == n:
        return 1
    else:
        return comb(n-1,r-1) + comb(n-1,r)

n = int(input('N: '))
r = int(input('R: '))

print(str(n)+'C'+str(r)+' = '+str(comb(n,r)))
