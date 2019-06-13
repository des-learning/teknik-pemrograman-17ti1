package main;

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func counting(name string, n int) {
	d, _ := time.ParseDuration(fmt.Sprintf("%dms", rand.Intn(1000)))
	for i := 0; i < n; i++ {
		fmt.Printf("Thead %s: %d ", name, i)
		time.Sleep(d)
	}
}

func main() {
	names := []string{"budi", "agus", "iwan", "susi"}
	var wg sync.WaitGroup

	wg.Add(len(names))
	for _, name := range names {
		go func(name string) {
			defer wg.Done()
			counting(name, 10)
		}(name)
	}

	wg.Wait()
}
