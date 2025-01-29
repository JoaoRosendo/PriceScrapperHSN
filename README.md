# PriceScraperHSN

This project is a web scraper built with Playwright to automate extracting price data from a website, to keep track of the price of a specific product.

## Steps

- Accepts cookie banners
- Clicks the button for "2Kg"
- Extracts the data-price-unit value
- Saves a screenshot and page source

## Installation
Install dependencies:
```sh
pip install playwright
playwright install
```
Run the scraper:
```sh
python HSN_price_scraper.py
```