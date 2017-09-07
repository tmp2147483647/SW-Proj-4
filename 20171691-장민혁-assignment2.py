num = 0 
factorial = 1

 
while 1:
    num = int(input("Enter a number "))
    if num == -1:
        break
    else:
        for i in range(1,num+1):
            factorial = i*factorial
        print(str(num)+ "!" , "=" ,factorial)
        factorial = 1
