def fac(n):
    j = 1
    for i in range(1,n+1):
        j = j * i
    return j

n = int(input())

while n != -1 :
    print(fac(n))
    n = int(input())
