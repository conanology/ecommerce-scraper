#!/usr/bin/env python3
"""
E-Commerce Product Scraper

Python scraper for extracting product information (name, price, rating)
from e-commerce sites. Exports to CSV/Excel.

Default target: books.toscrape.com (a site designed for web scraping practice)
Can be customized for other e-commerce sites.

Usage:
    python main.py --url <target_url>
    python main.py --url "https://books.toscrape.com/"
"""

import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path


def scrape_data(url):
    """
    Main scraping logic - Scrapes product data from e-commerce sites

    Args:
        url: Target URL to scrape

    Returns:
        pandas.DataFrame: Scraped data with columns: name, price, rating, availability, url
    """
    # Set headers to avoid bot detection
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    # books.toscrape.com structure (default example site)
    # This site is designed for web scraping practice
    products = soup.select('article.product_pod')

    if products:
        # books.toscrape.com format
        for product in products:
            try:
                name = product.select_one('h3 a')['title']
                price = product.select_one('p.price_color').text.strip()
                rating = product.select_one('p.star-rating')['class'][1]
                availability = product.select_one('p.availability').text.strip()
                product_url = product.select_one('h3 a')['href']

                data.append({
                    'name': name,
                    'price': price,
                    'rating': rating,
                    'availability': availability,
                    'url': product_url
                })
            except (AttributeError, KeyError, IndexError):
                continue

    # If no data found with books.toscrape structure, try generic patterns
    if not data:
        # Try generic product card patterns
        for item in soup.select('[class*="product"], [class*="item"]')[:20]:
            try:
                name_elem = item.select_one('[class*="name"], [class*="title"], h3, h4')
                price_elem = item.select_one('[class*="price"]')

                if name_elem and price_elem:
                    data.append({
                        'name': name_elem.text.strip(),
                        'price': price_elem.text.strip(),
                        'rating': 'N/A',
                        'availability': 'Unknown',
                        'url': url
                    })
            except (AttributeError, KeyError):
                continue

    return pd.DataFrame(data)


def main():
    parser = argparse.ArgumentParser(description='E-Commerce Product Scraper')
    parser.add_argument(
        '--url',
        default='https://books.toscrape.com/',
        help='Target URL to scrape (default: books.toscrape.com)'
    )
    parser.add_argument('--output', default='output/results.csv', help='Output file path')

    args = parser.parse_args()

    # Auto-add https:// if missing
    url = args.url
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    print(f"Scraping {url}...")
    df = scrape_data(url)

    # Save to CSV
    output_path = Path(args.output)
    output_path.parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"[OK] Scraped {len(df)} items")
    print(f"[OK] Saved to {output_path}")

    # Display sample
    if len(df) > 0:
        print("\n[DATA] Sample data:")
        print(df.head())


if __name__ == '__main__':
    main()
