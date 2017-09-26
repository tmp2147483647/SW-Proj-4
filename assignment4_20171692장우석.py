def change(n,m):
    while n < 0 or m < 0 or n<m: #음수이거나 n<m이면 입력을 다시 받기
        print("Wrong number")
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
    
    tmp=0
    tmp=n-m
    if tmp != 0 and m > tmp: # r을 작은 수로 바꾸기
        m=tmp
    return n,m

def combination(n,m):
    if m == 0 or n == m:
        return 1

    else:
        return combination(n-1,m-1) + combination(n-1,m)
    



n = int(input("Enter n: "))
m = int(input("Enter m: "))
n,m = change(n,m)
solution = combination(n,m)
print(n,"C",m,"=",solution)
