from string import ascii_lowercase

def is_isogram(string):
    string = string.lower()
    string = [char for char in string if char in ascii_lowercase]
    return (len(set(string)) == len(string))