package helpers

import (
	"math"
	"sort"
)

func Factors(n int) []int {
	if n <= 0 {
		return []int{} // Factors are typically for positive integers
	}
	factors := make(map[int]bool)

	// Iterate from 1 up to the square root of n
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			factors[i] = true
			factors[n/i] = true // Automatically get the complementary factor
		}
	}

	// Convert the map keys to a slice for sorting and return
	// This also handles duplicate factors (e.g., sqrt of perfect squares)
	result := make([]int, 0, len(factors))
	for f := range factors {
		result = append(result, f)
	}
	sort.Ints(result) // Optional: sort the factors in ascending order

	return result
}
