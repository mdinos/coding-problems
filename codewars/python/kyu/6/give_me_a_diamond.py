# https://www.codewars.com/kata/5503013e34137eeeaa001648

def diamond(n):
    if type(n) != int or n < 1 or n % 2 == 0:
        return None
    i = 1
    result = ""
    while i <= n:
        result += (" " * ((n - i) // 2))
        result += ("*" * i) + "\n"
        i += 2
    i -= 4
    while i >= 1:
        result += (" " * ((n - i) // 2))
        result += ("*" * i) + "\n"
        i -= 2
    return result