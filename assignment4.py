## factorial by recursive function
import sys
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return factorial(num-1) * num


def input_numbers():
    n = int(input("type n of nCr: "))
    r = int(input("type r of nCr: "))
    if n<r or n <= 0 or r < 0:
        print("wrong number!!")
        n,r = input_numbers()
    return n,r

while 1:
    n,r = input_numbers()
    fac_n = factorial(n)
    fac_r = factorial(r)
    fac_nr = factorial(n-r)
    result = fac_n/(fac_r*fac_nr)
    print(n, "C", r, "=", result)