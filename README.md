# E-Commerce Product Scraper

![Python](https://img.shields.io/badge/-Python-blue) ![BeautifulSoup4](https://img.shields.io/badge/-BeautifulSoup4-blue) ![Pandas](https://img.shields.io/badge/-Pandas-blue) ![Requests](https://img.shields.io/badge/-Requests-blue)

Python scraper for extracting product information (name, price, rating) from e-commerce sites. Exports to CSV/Excel.

## Features

- Scrapes product listings with pagination
- Extracts name, price, rating, URL
- Handles multiple e-commerce templates
- Exports to CSV and Excel
- Error handling and retry logic

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ecommerce-scraper.git
cd ecommerce-scraper

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Default: Scrapes books.toscrape.com (practice site)
python main.py

# Custom URL
python main.py --url "https://example.com" --output output/results.csv
```

**Live Demo:** Try it now with the default URL to see real data collection in action!

```bash
python main.py
# Collects 20+ products with name, price, rating, availability
```

## Output Format

Results are saved as CSV with the following columns:

| Column | Description |
|--------|-------------|
| name   | Item name   |
| value  | Item value  |
| url    | Source URL  |

## Testing

```bash
pytest tests/
```

## License

MIT License

## Contact

For questions or custom scraping projects, contact me at [your-email]

---

**Note:** This project uses books.toscrape.com as the default target, a website specifically designed for web scraping practice. The scraper is fully functional and collects real data. The code can be customized for other e-commerce sites by adjusting CSS selectors. Always respect robots.txt and Terms of Service when scraping websites.
