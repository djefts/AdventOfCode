package main

import (
	"fmt"
	"path/filepath"
	"strconv"
	"strings"

	"helpers"
)

func main() {
	//path, _ := filepath.Abs("./test")
	path, _ := filepath.Abs("./input")
	input := helpers.ReadInput(path)
	partOne(input)
	fmt.Println()
	partTwo(input)
}

func partOne(input []string) {
	var ranges []string
	breakPoint := -1
	for i, line := range input {
		if line != "" {
			ranges = append(ranges, line)
		} else {
			breakPoint = i
			break
		}
	}
	fmt.Println("Fresh Ingredient Ranges:", ranges)

	var ingredients []string
	for i := breakPoint + 1; i < len(input); i++ {
		ingredients = append(ingredients, input[i])
	}
	fmt.Println("List of ingredients:", ingredients)

	fresh := 0
	for _, ingredient := range ingredients {
		id, _ := strconv.Atoi(ingredient)
		for _, ingredientRange := range ranges {
			splitRange := strings.SplitN(ingredientRange, "-", 2)
			start, _ := strconv.Atoi(splitRange[0])
			end, _ := strconv.Atoi(splitRange[1])
			fmt.Println("\tChecking range:", start, "-", end)
			if id >= start && id <= end {
				fresh++
				break
			}
		}
	}
	fmt.Println("Answer:", fresh)
}

func partTwo(input []string) {
	var ranges []string
	for _, line := range input {
		if line != "" {
			ranges = append(ranges, line)
		} else {
			break
		}
	}
	fmt.Println("Fresh Ingredient Ranges:", ranges)

	unspoiled := make(map[int]struct{})
	for _, fresh := range ranges {
		splitRange := strings.SplitN(fresh, "-", 2)
		start, _ := strconv.Atoi(splitRange[0])
		end, _ := strconv.Atoi(splitRange[1])
		fmt.Println("\tBuilding set for range:", start, "-", end)
		for i := start; i <= end; i++ {
			unspoiled[i] = struct{}{}
			if i%5000000000 == 0 {
				fmt.Println("\t\t", i)
			}
		}
	}
	fmt.Println("Unspoiled ingredients:", unspoiled)
	fmt.Println("Answer:", len(unspoiled))
}
