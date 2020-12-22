def find_anagrams(word, candidates):
    anagrams = [candidate for candidate in candidates
                           if sorted(candidate.lower()) == sorted(word.lower())
                           and candidate.lower() != word.lower()]
    return anagrams
