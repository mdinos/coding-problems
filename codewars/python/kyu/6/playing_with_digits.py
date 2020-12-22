# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    nAsList = list(str(n))
    total = 0
    
    for num in nAsList:
        total += pow(int(num), p)
        p += 1
        
    if (total % n) == 0:
        return (total / n)
    else:
        return -1