# https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words=''):
    title_words_list = title.split(' ')
    minor_words_list = minor_words.split(' ')
    
    for i, word in enumerate(minor_words_list):
        minor_words_list[i] = word.lower()

    for i, word in enumerate(title_words_list):
        if word.lower() not in minor_words_list or i == 0:
            title_words_list[i] = word.capitalize()
        else:
            title_words_list[i] = word.lower()
            
    return (' '.join(title_words_list))