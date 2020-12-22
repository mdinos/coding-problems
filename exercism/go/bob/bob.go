// Package bob talks back to you
package bob

import "strings"

// IsItAQuestion detects if the strings ends in a question mark
func IsItAQuestion(remark string) bool {
	return string(remark[len(remark)-1]) == "?"
}

// IsItAllCaps detects whether the string is all capital letters
func IsItAllCaps(remark string) bool {
	return strings.ToUpper(remark) == remark && strings.ToLower(remark) != remark
}

// Hey gives you bob's responses
func Hey(remark string) string {
	remark = strings.TrimSpace(remark)
	switch {
	case remark == "":
		return "Fine. Be that way!"
	case IsItAQuestion(remark) == true && IsItAllCaps(remark) == true:
		return "Calm down, I know what I'm doing!"
	case IsItAllCaps(remark) == true:
		return "Whoa, chill out!"
	case IsItAQuestion(remark) == true:
		return "Sure."
	default:
		return "Whatever."
	}
}
