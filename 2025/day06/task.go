package main

import (
    "fmt"
    "path/filepath"
    "strings"
    "strconv"

    "helpers"
)

func main() {
	path, _ := filepath.Abs("./test")
    //path, _ := filepath.Abs("./input")
	input := helpers.ReadInput(path)
	partOne(input)
	fmt.Println()
	partTwo(input)
}

func partOne(input []string) {
    numProblems := len(strings.Fields(input[0]))
    fmt.Printf("There are %v problems.\n", numProblems)
    numLines := len(input)
    fmt.Printf("There are %v lines per problem.\n", numLines)
    total := 0
    operations := strings.Fields(input[numLines - 1])
    fmt.Println(operations)
    for i := 0; i < numProblems; i++ {
        calculation := 0
        summing := true
        if operations[i] == "*" {
            calculation = 1
            summing = false
        }
        for line := 0; line < len(input) - 1; line++ {
            vals := strings.Fields(input[line])
            val, _ := strconv.Atoi(vals[i])
            if summing {
                calculation += val
            } else {
                calculation *= val
            }
        }
        fmt.Printf("Problem #%v ", i + 1)
        if summing {
            fmt.Printf("sum: %v\n", calculation)
        } else {
            fmt.Printf("product: %v\n", calculation)
        }
        total += calculation
    }
    fmt.Println("Answer:", total)
}

func partTwo(input []string) {
    numProblems := len(strings.Fields(input[0]))
    fmt.Printf("There are %v problems.\n", numProblems)
    numLines := len(input)
    fmt.Printf("There are %v lines per problem.\n", numLines)
    total := 0
    operations := strings.Fields(input[numLines - 1])
    fmt.Println(operations)
    for i := 0; i < numProblems; i++ {
        calculation := 0
        summing := true
        if operations[i] == "*" {
            calculation = 1
            summing = false
        }
        // build up the numbers that make up the problem
        lineIndex := 0
        line0 := []rune(input[0])
        line1 := []rune(input[1])
        line2 := []rune(input[2])
        //line3 := []rune(input[3])
        number := []rune{line0[lineIndex], line1[lineIndex], line2[lineIndex]}
        fmt.Println("Build number", number)
        val, _ := strconv.Atoi(number)
        if summing {
            calculation += val
        } else {
            calculation *= val
        }

        fmt.Printf("Problem #%v ", i + 1)
        if summing {
            fmt.Printf("sum: %v\n", calculation)
        } else {
            fmt.Printf("product: %v\n", calculation)
        }
        total += calculation
    }
    fmt.Println("Answer:", total)
}
