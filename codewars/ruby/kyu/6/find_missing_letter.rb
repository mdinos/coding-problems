# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(arr)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    i = 0
    wasUppercase = false
    if arr[0].downcase != arr[0]
        arr.map!(&:downcase)
        wasUppercase = true
    end
    prevLetterIndex = alphabet.index(arr[0])
    missingLetterIndex = 0
    while i < arr.length do
        currentLetterIndex = alphabet.index(arr[i])
        puts currentLetterIndex
        if currentLetterIndex != (1 + prevLetterIndex)
            missingLetterIndex = currentLetterIndex
        end
        prevLetterIndex = currentLetterIndex
        i += 1
    end

    if wasUppercase == true
        return alphabet[missingLetterIndex - 1].upcase
    else
        return alphabet[missingLetterIndex - 1]
    end
end