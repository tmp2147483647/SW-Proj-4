num = 0 
sum = 0

 
while 1:
    num = int(input("Enter a number "))
    if num == 0:
        sum = 1
    elif num == -1:
        break
    for i in range(1,num+1):
        sum = sum + i
    print(str(num)+ "!" , "=" ,sum)
    sum = 0
