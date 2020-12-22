# https://www.codewars.com/kata/55466989aeecab5aac00003e

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    
    return_list = []
    
    min_val = min(lng, wdth)
    max_val = max(lng, wdth)
    
    while max_val > 0 and min_val > 0:
        return_list.append(min_val)
        max_val -= min_val
        if max_val < min_val:
            buffer = max_val
            max_val = min_val
            min_val = buffer
            
    return return_list
        