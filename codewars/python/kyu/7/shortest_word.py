# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

import sys

def find_short(s):
    ls = s.split(' ')
    l = sys.maxsize
    for word in ls:
        if len(word) <= l:
            l = len(word)
    return l