// 外部のプログラムの利用
package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("code", "sample.dat")
	err := cmd.Start()
    if err != nil {
		fmt.Println(err)
	}
	cmd.Wait()
}
