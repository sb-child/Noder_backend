package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		for {
			time.Sleep(10 * time.Second)
			fmt.Println("10 seconds")
		}
	}()
	go func() {
		for {
			time.Sleep(5 * time.Second)
			fmt.Println("5 seconds")
		}
	}()
	for {

	}
}
