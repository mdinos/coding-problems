// Package raindrops contains methods which match factors of
// numbers to raindrop sounds
package raindrops

import (
	"sort"
	"strconv"
)

// Convert converts an integer into rain sounds
// Looking at community solutions, the popular way is to use a struct
// to keep the list ordered, however I learned a lot this way so I
// thought I'd keep it.
func Convert(number int) string {
	var output string

	// Maps are unordered
	factorsAndSounds := map[int]string{
		3: "Pling",
		5: "Plang",
		7: "Plong",
	}

	// Must make a "slice" in order to iterate through the keys in order
	// Make a new slice with an inital size of 0, max size length of map
	factors := make([]int, 0, len(factorsAndSounds))

	// for each key in map append the key value to our slice
	for k := range factorsAndSounds {
		factors = append(factors, k)
	}

	// sort the keys by value
	sort.Ints(factors)

	for _, factor := range factors {
		if number%factor == 0 {
			output += factorsAndSounds[factor]
		}
	}

	if output == "" {
		output = strconv.Itoa(number)
	}
	return output
}
