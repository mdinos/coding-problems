// Package acronym contains methods for manipulating multi-word strings into acronyms.
package acronym

import (
	"strings"
	"unicode"
)

// FindFirstLetter finds first char in a-z
func FindFirstLetter(word string) string {
	var l string
	for i := 0; i < len(word); i++ {
		if unicode.IsLetter(rune(word[i])) {
			l = string(word[i])
			break
		}
	}
	return l
}

// RemoveSpecial Special chars to be removed
func RemoveSpecial(s string, chars []string) string {
	for _, char := range chars {
		s = strings.ReplaceAll(s, char, " ")
	}
	return s
}

// Abbreviate abberviates a phrase to an acronym
func Abbreviate(s string) string {
	// Remove extendable list of characters
	removalChars := []string{"-", "_"}
	s = RemoveSpecial(s, removalChars)

	words := strings.Fields(s)
	var product string
	for i := 0; i < len(words); i++ {
		word := words[i]
		l := FindFirstLetter(word)

		// ensure initialism is letters only
		if l != "" {
			product += l
		}
	}
	return strings.ToUpper(product)
}
