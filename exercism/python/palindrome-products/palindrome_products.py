def largest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError('Your minimum factor is bigger than your maximum factor')
    result = dict(value=0, factors=[])
    for factor_1 in range(max_factor, min_factor, -1):
        for factor_2 in range(max_factor, min_factor, -1):
            product = (factor_1 * factor_2)
            product_string = str(product)
            if product_string[::-1] == product_string and (result['value'] == 0 or product > result['value']):
                result = dict(value=product, factors={(factor_1, factor_2)})
            elif len(product_string) < len(str(result['value'])):
                break
    print(result)
    return result['value'], result['factors']

def smallest_palindrome(max_factor, min_factor):
    pass