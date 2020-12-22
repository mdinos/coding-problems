# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    numList = list(str(n))
    if (len(numList) == 1):
        return n
    else:
        val = 0
        for num in numList:
            val += int(num)
        while val >= 10:
            val = digital_root(val)
        return val