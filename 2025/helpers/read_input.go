package helpers

import (
	"bufio"
	"os"
)

func ReadInput(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		println(err.Error())
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {

		}
	}(file)

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}
