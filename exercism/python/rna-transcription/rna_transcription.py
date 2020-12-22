def to_rna(dna_strand):
    rna_strand = map(get_opposite, dna_strand)
    return ''.join(list(rna_strand))

def get_opposite(letter):
    if letter is 'G':
        return 'C'
    elif letter is 'C':
        return 'G'
    elif letter is 'T':
        return 'A'
    elif letter is 'A':
        return 'U'
    else:
        return ''