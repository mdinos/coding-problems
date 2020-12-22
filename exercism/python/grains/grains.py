def square(number):
    if number <= 64 and number >= 1:
        return pow(2, number - 1)
    else:
        raise ValueError('Number must be between 1 and 64')

def total(number):
    if number >= 65 or number <= 0:
        raise ValueError('Number must be between 1 and 64')

    total_list = [square(i) for i in range(1, number + 1)]
    return sum(total_list)