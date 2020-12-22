# https://www.codewars.com/kata/52c4dd683bfd3b434c000292

def is_interesting(number, awesome_phrases):
    if number == 98 or number == 99:
        return 1
    elif number < 100:
        return 0
        
    next_three = [number, number + 1, number + 2]
    
    xs = []
        
    xs.append([check_followed_by_zeros(i) for i in next_three])  
    xs.append([check_all_numbers_same(i) for i in next_three])
    xs.append([check_if_palindrome(i) for i in next_three])
    xs.append([check_awesome_phrases(i, awesome_phrases) for i in next_three])
    xs.append([check_ascending_digits(i) for i in next_three])
    xs.append([check_decending_digits(i) for i in next_three])
        
    for x in xs:
        if x[0]:
            return 2
    for x in xs:
        if x[1] or x[2]:
            return 1
    return 0
        
def check_followed_by_zeros(number):
    return (len(str(number)) - 1) * "0" == str(number)[1:len(str(number))]
        
def check_all_numbers_same(number):
    return str(number)[0] * len(str(number)) == str(number)
        
def check_if_palindrome(number):
    return str(number) == str(number)[::-1]

def check_awesome_phrases(number, awesome_phrases):
    return number in awesome_phrases
        
def check_ascending_digits(number):
    return str(number) in '1234567890'
    
def check_decending_digits(number):
    return str(number) in '9876543210'