# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(a):
    for i, n in enumerate(a):
        l = 0
        r = 0
        for j in range(0, i):
            l += a[j]
        for j in range(i + 1, len(a)):
            r += a[j]
        if l == r:
            return i
    return -1
        