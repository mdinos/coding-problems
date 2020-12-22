# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    indicesToRemove = []
    
    i = 0
    while True:
        if i >= (len(iterable) - 1):
            break
        elif iterable[i] == iterable[i+1]:
            indicesToRemove += [i+1]
        i += 1
        
    iterable = list(iterable)
    i = len(indicesToRemove) - 1
    
    while i >= 0:
        del iterable[indicesToRemove[i]]
        i -= 1
        
    return iterable
    