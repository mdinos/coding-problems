def raindrops(number: int):
    factors_and_pl_ngs = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    pl_ngs = [sound for divisor, sound in factors_and_pl_ngs if number % divisor == 0]
    return str(''.join(pl_ngs) or number)