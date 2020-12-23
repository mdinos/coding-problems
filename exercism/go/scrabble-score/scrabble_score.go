// Package scrabble helps you calculate your scrabble score
package scrabble

import (
	"strings"
)

// Score calculate your scrabble score
func Score(word string) int {
	var totalScore int
	scoresPerLetter := map[int][]string{
		1: {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"},
		2: {"D", "G"},
		3: {"B", "C", "M", "P"},
		4: {"F", "H", "V", "W", "Y"},
		5: {"K"},
		8: {"J", "X"},
		10: {"Q", "Z"},
	}
	
	for _, _letter := range word {
		letter := strings.ToUpper(string(_letter))
		for score, letterList := range scoresPerLetter {
			for _, l := range letterList {
				if letter == l {
					totalScore += score
				}
			}
		}
	}
	return totalScore
}
