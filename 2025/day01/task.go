package main

import (
	"fmt"
	"path/filepath"
	"strconv"

	"helpers"
)

func main() {
	//path, _ := filepath.Abs("./test")
	path, _ := filepath.Abs("./input")
	input := helpers.ReadInput(path)
	partOne(input)
	partTwo(input)
}

func partOne(input []string) {
	dial := 50
	//fmt.Println(dial)
	password := 0

	for _, rotation := range input {
		direction := rune(rotation[0])
		distance, _ := strconv.Atoi(rotation[1:])
		distance %= 100
		if direction == 'R' {
			//fmt.Println("Right", distance)
			dial += distance
			if dial > 99 {
				dial -= 100
			}
		} else if direction == 'L' {
			//fmt.Println("Left", distance)
			dial -= distance
			if dial < 0 {
				dial += 100
			}
		}

		//fmt.Println(dial)
		if dial == 0 {
			password += 1
		} else if dial > 99 || dial < 0 {
			panic("Invalid position!")
		}
	}
	fmt.Println("Answer:", password)
}

func partTwo(input []string) {
	// password method 0x434C49434B
	dial := 50
	//fmt.Println(dial)
	password := 0

	for _, rotation := range input {
		direction := rune(rotation[0])
		distance, _ := strconv.Atoi(rotation[1:])
		if distance >= 100 {
			password += distance / 100
			distance %= 100
		}
		if direction == 'R' {
			//fmt.Println("R", distance)
			dial += distance
			if dial > 99 {
				if dial == 100 {
					dial = 0
				} else {
					//fmt.Println("\t\tpassed")
					password += 1
					dial -= 100
				}
			}
		} else if direction == 'L' {
			//fmt.Println("L", distance)
			if dial == 0 {
				password -= 1
				//fmt.Println("\t\tunpassed")
			}
			dial -= distance
			if dial < 0 {
				//fmt.Println("\t\tpassed")
				password += 1
				dial += 100
			}
		}

		//fmt.Println(dial)
		if dial == 0 {
			password += 1
		} else if dial > 99 || dial < 0 {
			panic("Invalid position!")
		}
	}
	fmt.Println("Answer:", password)
}
