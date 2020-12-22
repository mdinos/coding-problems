def is_armstrong(number):
    number_len = len(str(number))
    number_iter = iter(str(number))
    numbers_to_add = []
    while True:
        try:
            numbers_to_add.append(pow(int(next(number_iter)), number_len))
        except StopIteration:
            break
    if sum(numbers_to_add) == number:
        return True
    else:
        return False