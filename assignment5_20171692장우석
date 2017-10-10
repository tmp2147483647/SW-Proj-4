import time
def fibo(n):    
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
def iterfibo(n):    
    fibo = []    
    for i in range(0, n+1):        
        if i == 0:            
            fibo.append(0)        
        elif i == 1:            
            fibo.append(1)
        else:            
            fibo.append(fibo[i-1] + fibo[i-2])                      
    return fibo[n]
#Value 에러제거 ex) 1.1 or String
while True:    
    try:        
        n = int(input())        
        break    
    except ValueError:        
        print("Value Error")
#-1이아닌 음의 정수 제거   
while n != -1 and n < 0:    
    print("n<0")    
    n = int(input())
while n != -1:    
    solution =iterfibo(n)    
    print("iterfibo(%d)=%d"%(n, solution))
    """
    ts = time.time()
    fibonumber = iterfibo(n)    
    ts = time.time() - ts
    print("iterfibo(%d)=%d, time %.6f" %(n, fibonumber,ts))    
    ts = time.time()
    fibonumber = fibo(n)    
    ts = time.time() - ts
    print("fibo(%d)=%d, time %.6f" %(n, fibonumber,ts))    
    """
     while True:        
            try:            
                n = int(input())            
                break        
            except ValueError:            
                print("Value Error")
                
      while n != -1 and n < 0 :
         print("n<0")
         n = int(input())        
