def verify(isbn):
    filtered_isbn = list(''.join(isbn.split('-')))
    result_list = []
    if len(filtered_isbn) != 10:
        return False
    if filtered_isbn[-1] == 'X':
        filtered_isbn[-1] = 10
    for i, j in enumerate(range(10, 0, -1)):
        try:
            if filtered_isbn[i] != 'X':
                result_list.append(int(filtered_isbn[i]) * j)
        except:
            return False
    if sum(result_list) % 11 == 0:
        return True
    return False
