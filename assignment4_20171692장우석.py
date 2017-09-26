def combination(n,m):

    if m == 0 or n == m:
        return 1

    else:
        return combination(n-1,m-1) + combination(n-1,m)
    



n = int(input("Enter n: "))
m = int(input("Enter m: "))
solution = combination(n,m)
print(n,"C",m,"=",solution)
