def factorials(x):
    if x == 1:
        return 1
 
    return x * factorials(x - 1)

while True:
    L = int(input('숫자 입력: '))

    if(L == -1):
        break
    else:
        print("{0}! = {1}".format(L, factorials(L)))
