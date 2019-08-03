def two_sum(xs, target_value):
    for i, x in enumerate(xs):
        combinations = [x + y for y in xs if xs.index(y) != i]
        print('combinations: {}'.format(combinations))
        if target_value in combinations:
            return True
    return False
    
print(two_sum([7, 1, -3, 2, 4], 5))