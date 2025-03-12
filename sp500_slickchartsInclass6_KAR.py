import scrapy
import csv

class Sp500SlickchartsSpider(scrapy.Spider):
    name = "sp500_slickcharts"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500"]

    def parse(self, response):
        self.log("Scraping has started...")

        # Select all table rows
        rows = response.css("table.table tbody tr")

        # Check if any data was found
        if not rows:
            self.log("No rows found! The website may be blocking Scrapy.")
            return

        # Initialize list for data storage
        data = []

        for row in rows:
            number = row.css("td:nth-child(1)::text").get()
            company = row.css("td:nth-child(2) a::text").get()
            symbol = row.css("td:nth-child(3) a::text").get()
            ytd_return = row.css("td:nth-child(6)::text").get()

            if number and company and symbol and ytd_return:
                data.append({
                    "Rank": number.strip(),
                    "Company": company.strip(),
                    "Symbol": symbol.strip(),
                    "YTD Return": ytd_return.strip()
                })

        # Save data to CSV
        if data:
            with open("sp500_performance.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Rank", "Company", "Symbol", "YTD Return"])
                writer.writeheader()
                writer.writerows(data)

            self.log("Data successfully saved to sp500_performance.csv")
        else:
            self.log("No data was scraped.")
