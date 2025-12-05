package main

import (
	"fmt"
	"helpers"
	"path/filepath"
	"strings"
)

func main() {
	//path, _ := filepath.Abs("./test")
	path, _ := filepath.Abs("./input")
	input := helpers.ReadInput(path)
	partOne(input)
	fmt.Println()
	partTwo(input)
}

func partOne(input []string) (int, []string) {
	output := append([]string(nil), input...)
	accessible := 0
	for i, line := range input {
		fmt.Println(line)
		for j, spot := range line {
			if spot == '@' {
				// count the rolls in a 3x3 grid centered at [i, j]
				nearby := 0
				for row := i - 1; row <= i+1; row++ {
					if row < 0 || row >= len(input) {
						continue
					}
					for col := j - 1; col <= j+1; col++ {
						if col < 0 || col >= len(input[row]) {
							continue
						}
						if input[row][col] == '@' {
							nearby++
						}
					}
				}
				if nearby < 5 {
					//fmt.Printf("[%v, %v] is safe\n", i, j)
					outLine := []rune(output[i])
					outLine[j] = 'x'
					output[i] = string(outLine)
					accessible++
				}
			}
		}
	}
	fmt.Println()
	fmt.Println(strings.Join(output, "\n"))
	fmt.Println("Answer:", accessible)
	return accessible, output
}

func partTwo(input []string) {
	accessible := 0
	removed, cleaned := partOne(input)
	accessible += removed
	fmt.Println("Removed:", removed, "\nRemaining:\n", strings.Join(cleaned, "\n"))
	for removed > 0 {
		removed, cleaned = partOne(cleaned)
		accessible += removed
	}
	fmt.Println("Final Answer:", accessible)
}
