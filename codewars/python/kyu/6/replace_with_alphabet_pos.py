# https://www.codewars.com/kata/546f922b54af40e1e90001da

def get_index(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter not in alphabet:
        return ''
    else:
        return str(alphabet.index(letter) + 1)
    
def alphabet_position(text):
    text = iter(text.lower())
    list_of_nums = list(map(get_index, text))
    list_of_nums = [i for i in list_of_nums if i != '']
    
    return ' '.join(list_of_nums)