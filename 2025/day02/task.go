package main

import (
	"fmt"
	"path/filepath"
	"strconv"
	"strings"
	"unicode/utf8"

	"helpers"
)

func main() {
	//path, _ := filepath.Abs("./test")
	path, _ := filepath.Abs("./input")
	input := strings.Split(helpers.ReadInput(path)[0], ",")
	//partOne(input)
	partTwo(input)
}

func partOne(input []string) {
	fmt.Println(input)

	runningSum := 0
	for _, idRange := range input {
		parts := strings.Split(idRange, "-")
		start, end := parts[0], parts[1]
		si, _ := strconv.Atoi(start)
		ei, _ := strconv.Atoi(end)
		fmt.Print(start, " ", end, " --> ")
		for i := si; i <= ei; i++ {
			index := strconv.Itoa(i)
			length := utf8.RuneCountInString(index)
			if length%2 == 0 {
				// only bother to check even numbers
				if index[0:length/2] == index[length/2:] {
					fmt.Print(i, "  ")
					runningSum += i
				}
			}
		}
		fmt.Println()
	}
	fmt.Println("Answer:", runningSum)
}

func partTwo(input []string) {
	fmt.Println(input)
	factors := make(map[int][]int)
	for i := 2; i <= 10; i++ {
		facs := helpers.Factors(i)
		factors[i] = facs[:len(facs)-1]
	}
	fmt.Println(factors)
	runningSum := 0
	// loop through the set of id ranges
	for _, idRange := range input {
		parts := strings.Split(idRange, "-")
		start, end := parts[0], parts[1]
		si, _ := strconv.Atoi(start)
		ei, _ := strconv.Atoi(end)
		fmt.Println(start, " --> ", end)

		// loop through the product IDs in range
	productsLoop:
		for productID := si; productID <= ei; productID++ {
			//fmt.Println(productID, "  ")
			index := strconv.Itoa(productID)
			length := utf8.RuneCountInString(index) // number of digits in the product ID
			// check if the product ID is a properly repeated sequence of digits
			for _, sequenceLength := range factors[length] {
				strID := strconv.Itoa(productID)
				multiplyString := strings.Repeat(strID[0:sequenceLength], length/sequenceLength)
				if multiplyString == strID {
					fmt.Println(sequenceLength, "*", length/sequenceLength, "::", multiplyString, "vs", strID)
					fmt.Println("\t", productID)
					runningSum += productID

					// skip so it doesn't count multi-repeating sequences multiple times
					//    e.g., '222222' is '2' 6 times, '22' 3 times, and '222' 2 times
					continue productsLoop
				}
			}
		}
		fmt.Println()
	}
	fmt.Println("Answer:", runningSum)
}
