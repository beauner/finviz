package main

import (
	"flag"
	"fmt"
	"log"

	"github.com/PuerkitoBio/goquery"
)

var ticker string

func ExampleScrape() {
	flag.StringVar(&ticker, "ticker", "AAPL", "Symbol/Stock of which float to query")
	flag.Parse()

	url := "http://finviz.com/quote.ashx?t=" + ticker
	doc, err := goquery.NewDocument(url)
	if err != nil {
		log.Fatal(err)
	}
	indexes := make(map[int]string)
	values := make(map[int]string)
	combined := make(map[string]string)
	doc.Find(".snapshot-table2").Each(func(i int, s *goquery.Selection) {

		s.Find(".snapshot-td2-cp").Each(func(i int, ss *goquery.Selection) {

			indexes[i] = ss.Text()
			//fmt.Printf("indexes: %v", indexes)
		})
		s.Find(".snapshot-td2").Each(func(i int, ss *goquery.Selection) {

			values[i] = ss.Text()
			//fmt.Printf("values: %v", values)
		})
		for i, v := range indexes {
			combined[v] = values[i]
		}
		fmt.Printf("Float for %s = %v\n", ticker, combined["Shs Float"])
	})
}

func main() {
	ExampleScrape()
}
