package main

import (
	"fmt"
	"log"

	"github.com/PuerkitoBio/goquery"
)

// http://finviz.com/screener.ashx?v=111&f=earningsdate_todaybefore,sh_avgvol_o200,sh_relvol_o1.5,ta_perf_d5o&ft=4 #Earnings Breakout
func ExampleScrape() {
	url := "http://finviz.com/screener.ashx?v=111&f=sh_avgvol_o200,sh_relvol_o1.5,ta_perf_d5o&ft=4"
	doc, err := goquery.NewDocument(url)
	if err != nil {
		log.Fatal(err)
	}
	symbols := make(map[int]string)
	doc.Find(".screener-body-table-nw").Each(func(i int, s *goquery.Selection) {

		symbol := s.Find(".screener-link-primary").Text()
		if symbol != "" {
			symbols[i] = symbol
			fmt.Printf("Symbol = %s\n", symbol)
		}

	})

}

func main() {
	ExampleScrape()
}
