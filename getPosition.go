package main

import (
	"flag"
	"fmt"
)

func main() {
	var price float64
	var quantity float64
	flag.Float64Var(&price, "price", 12.34, "Current Price")
	flag.Float64Var(&quantity, "quantity", 100, "# of Shares")
	flag.Parse()

	fmt.Printf("Price: $%v \n", price)

	targetPrice := price * 1.15
	fmt.Printf("Target Price: $%.2f \n", targetPrice)

	stopPrice := price - (price * 0.07)
	fmt.Printf("Stop Price: $%.2f \n", stopPrice)

	investment := price * quantity
	fmt.Printf("Investment Cost: $%.2f \n", investment)

}
