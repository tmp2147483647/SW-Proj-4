import time

def iterfibo():
    if n <= 1:
        return n
    return iterfibo(n - 1) + iterfibo(n - 2)






while True:
    nbr = int(input("Enter a number:"))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    
