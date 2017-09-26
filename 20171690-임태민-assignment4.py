import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

n = int(input('N: '))
r = int(input('R: '))

print(str(n)+'C'+str(r)+' = '+str(ncr(n,r)))
