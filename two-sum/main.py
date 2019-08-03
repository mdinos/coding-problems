def two_sum(xs: list, target_value: int):
    """
        Return whether or not there are two numbers in the list that add up to k.
        :returns: bool
    """
    for i, x in enumerate(xs):
        combinations = [x + y for j, y in enumerate(xs) if j != i]
        print('combinations: {}'.format(combinations))
        if target_value in combinations:
            return True
    return False

print(two_sum([7, 1, -3, 2, 4], 5))