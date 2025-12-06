package main

import (
	"fmt"
	"path/filepath"
	"strconv"
	"strings"
	"slices"

	"helpers"
)

func main() {
	//path, _ := filepath.Abs("./test")
    //path, _ := filepath.Abs("./test2")
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
			//fmt.Println("\tChecking range:", start, "-", end)
			if id >= start && id <= end {
				fresh++
				break
			}
		}
	}
	fmt.Println("Answer:", fresh)
}

func partTwo(input []string) []string {
	var ranges []string
	for _, line := range input {
		if line != "" {
			ranges = append(ranges, line)
		} else {
			break
		}
	}
	fmt.Println("Fresh Ingredient Ranges:", ranges)
	ranges = bubbleSort(ranges)
	fmt.Println("Sorted Ingredient Ranges:", ranges)

    fmt.Println("INITIAL CHECK!")
	unspoiled, diffs := cleanIntersections(ranges)
	for diffs > 0 {
		fmt.Printf("RECHECKING! There were %v overlaps\n", diffs)
		unspoiled, diffs = cleanIntersections(unspoiled)
	}

	fmt.Println("Unspoiled ingredients:", unspoiled)
	totalIngredients := 0
	for _, rang := range unspoiled {
		splitRange := strings.SplitN(rang, "-", 2)
		start, _ := strconv.Atoi(splitRange[0])
		end, _ := strconv.Atoi(splitRange[1])
		totalIngredients += end - start + 1
	}
	fmt.Println("Answer:", totalIngredients)
	return nil
}

func bubbleSort(input []string) []string {
	n := len(input)
	swapped := true

	for swapped {
		swapped = false
		for i := 0; i < n-1; i++ {
			splitCurr := strings.SplitN(input[i], "-", 2)
			curr, _ := strconv.Atoi(splitCurr[0])
			splitNext := strings.SplitN(input[i+1], "-", 2)
			next, _ := strconv.Atoi(splitNext[0])
			// Compare adjacent elements and swap if the first is greater than the second
			if curr > next {
				input[i], input[i+1] = input[i+1], input[i]
				swapped = true
			}
		}
		// After each pass, the largest unsorted element is in its correct place at the end
		n--
	}
	return input
}

func cleanIntersections(ranges []string) ([]string, int) {
	totalIntersections := 0
	for i := 0; i < len(ranges)-1; i++ {
		intersections := 0
		splitIRange := strings.SplitN(ranges[i], "-", 2)
		iStart, _ := strconv.Atoi(splitIRange[0])
		iEnd, _ := strconv.Atoi(splitIRange[1])
		for j := i + 1; j < len(ranges); j++ {
			splitJRange := strings.SplitN(ranges[j], "-", 2)
			jStart, _ := strconv.Atoi(splitJRange[0])
			jEnd, _ := strconv.Atoi(splitJRange[1])
            // check for intersection of range I with range J
			if (iStart >= jStart && iStart <= jEnd) || (iEnd >= jStart && iEnd <= jEnd) || (jStart >= iStart && jStart <= iEnd) || (jEnd >= iStart && jEnd <= iEnd) {
			    // calculate the new range
                newRange := fmt.Sprintf("%v-%v", min(iStart, jStart), max(iEnd, jEnd))
                ranges[i] = newRange
                // delete the intersecting range
                ranges = slices.Delete(ranges, j, j+1)
                // track
                intersections++
            }
        }
        totalIntersections += intersections
        fmt.Printf("\tFound %v overlaps with range %v\n", intersections, splitIRange)
	}
	return ranges, totalIntersections
}
