mapping = {   
        'AUG' : 'Methionine',
        'UUU' : 'Phenylalanine',
        'UUC' : 'Phenylalanine',
        'UUA' : 'Leucine',
        'UUG' : 'Leucine',
        'UCU' : 'Serine',
        'UCC' : 'Serine',
        'UCA' : 'Serine',
        'UCG' : 'Serine',
        'UAU' : 'Tyrosine', 
        'UAC' : 'Tyrosine', 
        'UGU' : 'Cysteine', 
        'UGC' : 'Cysteine',
        'UGG' : 'Tryptophan',
        'UAA' : 'STOP',
        'UAG' : 'STOP', 
        'UGA' : 'STOP'
    }

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protiens = []
    i = 0
    while True:
        try:
            if mapping[codons[i]] != 'STOP':
                protiens.append(mapping[codons[i]])
            else:
                break
        except:
            break
        i += 1
    return protiens
    