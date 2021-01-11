// Package luhn contains functions for validation of certain identification
// numbers
package luhn

import (
	"strconv"
	"strings"
)

// Valid checks whether number is valid luhn number
func Valid(number string) bool {

	// strip whitespace and ensure string is valid number for checksum ops
	number = strings.ReplaceAll(number, " ", "")
	if _, err := strconv.Atoi(number); err != nil || len(number) <= 1 {
		return false
	}

	// transform number to slice
	numberSlice := make([]int, 0, len(number))
	for _, i := range number {
		n, err := strconv.Atoi(string(i))
		if err != nil {
			panic(err)
		}
		numberSlice = append(numberSlice, n)
	}

	// check against luhn algo
	for i := len(numberSlice) - 2; i >= 0; i -= 2 {
		n := numberSlice[i]
		n = n * 2
		if n > 9 {
			n = n - 9
		}
		numberSlice[i] = n
	}

	var sum int
	for _, i := range numberSlice {
		sum += i
	}

	if sum%10 == 0 {
		return true
	}
	return false
}
