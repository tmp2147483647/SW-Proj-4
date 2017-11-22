from math import factorial as fact


romans = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100:'C', 90:'XC', 50:'L', 40:'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
    1: 'I'
}

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr)
        r = "0b" + str(n)
    except:
        r = "Error!"

    return int(r, 2)

def decToRoman(numStr):
    try:
        n = int(numStr)
        result = ""
        for value in sorted(romans.keys(), reverse=True):
            while n >= value:
                result += romans[value]
                n -= value
    except:
        result = "Error!"
    return result

def romanToDec(Str):
    try:
        tmp = 0
        for value in sorted(romans.keys(), reverse=True):
            check = len(romans[value])
            while (Str[0:check] == romans[value]):
                Str = Str.replace(romans[value], "", 1)
                tmp += value

            """
            while(check == 1 and Str[0:check] == romans[value]):
                Str = Str.replace(romans[value], "", 1)
                tmp += value

            while (check == 2 and Str[0:check] == romans[value]):
                Str = Str.replace(romans[value], "", 1)
                tmp += value
            """

    except:
        tmp = "Error!"
    return tmp
function_Dic = {
    'factorial (!)': factorial,
    '-> binary': decToBin,
    'binary -> dec': binToDec,
    '-> roman': decToRoman,
    'roman -> dec': romanToDec,
}

'''
functionMap = [
    ('factorial (!)', factorial),
    ('-> binary', decToBin),
    ('binary -> dec', binToDec),
    ('-> roman', decToRoman),
    ('roman -> dec', decToRoman),
]
'''
