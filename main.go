package main

import (
	"embed"
	"fmt"
	"io/fs"

	"time"
)

//go:embed 100MB.bin
var bigFile embed.FS

func main() {
	fmt.Println("this version is 0.0.2")
	time.Sleep(time.Minute)
	//Not working code, only increase binary file size
	data, err := fs.ReadFile(bigFile, "100MB.bin")
	if err != nil {
		fmt.Println("Failed to read embedded file:", err)
		return
	}

	fmt.Println("Loaded data length:", len(data))
}
