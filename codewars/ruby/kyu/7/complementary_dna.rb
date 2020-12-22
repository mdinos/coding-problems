# https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna)
    dnaArr = dna.split('')
    i = 0
    while i < dnaArr.length do
      letter = dnaArr[i]
      case letter
      when 'A'
        letter = 'T'
      when 'T'
        letter = 'A'
      when 'C'
        letter = 'G'
      when 'G'
        letter = 'C'
      else
        letter = ''
      end
      dnaArr[i] = letter
      i += 1
    end
    return dnaArr.join()
  end