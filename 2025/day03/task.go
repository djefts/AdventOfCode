package main

import (
	"fmt"
	"helpers"
	"math"
	"path/filepath"
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
	totalJoltage := 0
	for _, bank := range input {
		fmt.Println(bank)
		tens := 1
		tensPlace := 0
		for i := 0; i < len(bank)-1; i++ {
			battery := int(bank[i] - '0')
			if battery > tens {
				tens = battery
				tensPlace = i
			}
		}
		onesPlace := tensPlace + 1
		ones := int(bank[onesPlace] - '0')
		for i := onesPlace; i < len(bank); i++ {
			battery := int(bank[i] - '0')
			if battery > ones {
				ones = battery
				onesPlace = i
			}
		}
		joltage := tens*10 + ones
		fmt.Println(joltage)
		totalJoltage += joltage
	}
	fmt.Println("Answer:", totalJoltage)
}

func partTwo(input []string) {
	totalJoltage := 0.0
	for _, bank := range input {
		fmt.Println(bank)
		joltage := 0.0
		digit := 0
		digitPlace := 0
		for digitNum := 11; digitNum >= 0; digitNum-- {
			//fmt.Printf("Searching for digit #%v in %v\n", 12-digitNum, bank[digitPlace:len(bank)-digitNum])
			for i := digitPlace; i < len(bank)-digitNum; i++ {
				battery := int(bank[i] - '0')
				if battery > digit {
					digit = battery
					digitPlace = i + 1
				}
			}
			power := math.Pow(10, float64(digitNum))
			//fmt.Printf("\tFound %v. Adding on %.0f\n", digit, float64(digit)*power)
			joltage += float64(digit) * power
			digit = 0
			//fmt.Println(math.Pow(10, float64(digitNum)))
		}
		fmt.Printf("\t%0.f\n", joltage)
		totalJoltage += joltage
	}
	fmt.Printf("Answer: %.0f\n", totalJoltage)
}
