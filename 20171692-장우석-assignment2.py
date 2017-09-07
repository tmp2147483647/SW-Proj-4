def fac(n):
    if n < 0:
        print("Please enter only positive integers.")
    else:
        j = 1
        for i in range(1,n+1):
            j = j * i
        print(j)
  

n = int(input())

while n != -1 :
    fac(n)
    n = int(input())
