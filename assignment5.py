import time

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo (n-2)


def iterfibo(n):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append(answer[i - 1] + answer[i - 2])
    if n == 0:
        return n
    else:
        return answer[-1]



n = int(input("input number: "))
if n < 0:
    print("n must be bigger than 0")

ts = time.time()
fibonumber = iterfibo(n)
ts = time.time() - ts
print("IterFibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
ts = time.time()
fibonumber = fibo(n)
ts = time.time() - ts
print("Fibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
