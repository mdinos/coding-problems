package main

import (
	"fmt"
)

func getSubsets(xs []int, k int, start int, currentLength int, used [4]bool) {
	if (currentLength == k) {
		var combo []int
		for i := 0; i < len(xs); i++ {
			if (used[i] == true) {
				combo = append(combo, xs[i])
			}
		}
		fmt.Println(" ")
		fmt.Println(combo)
		return;
	}
	if (start == len(xs)) {
		return;
	}
	// For every index we have two options,
	// 1.. Either we select it, means put true in used[] and make currLen+1
	used[start] = true;
	getSubsets(xs, k, start + 1, currentLength + 1, used);
	// 2.. OR we dont select it, means put false in used[] and dont increase
	// currLen
	used[start] = false;
	getSubsets(xs, k, start + 1, currentLength, used);
}

func maxProduct(xs []int) {
	var bools [4]bool
    getSubsets(xs, 3, 0, 0, bools)
	//for index, element := range xs {
	//	
	//}
	fmt.Println(xs)
}

func main() {
	xs := []int{4, -4, 2, 8}
	maxProduct(xs)
}