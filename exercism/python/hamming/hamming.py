def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of the same length.')
    xs = zip(strand_a, strand_b)
    hd = [(s, t) for (s, t) in xs if s == t]
    return len(strand_a) - len(hd)
