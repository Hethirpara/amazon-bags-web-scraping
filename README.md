# Amazon Bags Scraper

## Overview

This Python script scrapes product information from the Amazon India website for bags. It collects data such as product URLs, names, prices, ratings, and the number of reviews from the first 20 pages of search results and saves the information into a CSV file.

## Features

- **Product URLs:** Extracts the URL for each product.
- **Product Names:** Gathers the names of the products.
- **Product Prices:** Retrieves the price of each product.
- **Ratings:** Collects the average customer rating.
- **Number of Reviews:** Gets the total number of customer reviews for each product.

## Libraries Used

- `requests`: For sending HTTP requests to Amazon's servers.
- `BeautifulSoup`: For parsing and navigating the HTML content.
- `pandas`: For organizing the scraped data into a DataFrame and exporting it to a CSV file.
- `time`: For adding delays between requests to avoid being blocked by Amazon.

## Usage

1. **Install Dependencies:** Make sure you have `requests`, `beautifulsoup4`, and `pandas` installed.
    ```bash
    pip install requests beautifulsoup4 pandas
    ```
2. **Run the Script:** Execute the script in your Python environment.
    ```bash
    python amazon_bags_scraper.py
    ```
3. **Output:** The script will create a `scraped_data.csv` file in the same directory, containing the scraped data.

## How It Works

1. **HTTP Requests:** The script sends GET requests to the Amazon search results pages for bags.
2. **HTML Parsing:** BeautifulSoup parses the HTML content of each page.
3. **Data Extraction:** The script identifies and extracts relevant data points (URLs, names, prices, ratings, review counts) from each product listing.
4. **Data Storage:** The extracted data is stored in lists.
5. **DataFrame Creation:** The data is organized into a pandas DataFrame.
6. **CSV Export:** The DataFrame is exported to a CSV file named `scraped_data.csv`.

## Important Notes

- **Respect Terms of Service:** Be mindful of Amazon's terms of service when scraping data.
- **Avoid Overloading:** The script includes a delay between requests to prevent overloading Amazon's servers and avoid getting blocked.
- **Error Handling:** The script includes basic error handling to manage exceptions that may occur during the scraping process.

## Future Enhancements

- **Dynamic Page Range:** Allow users to specify the number of pages to scrape.
- **Additional Data Points:** Extract more detailed information about each product, such as seller details or product descriptions.
- **Improved Error Handling:** Enhance error handling for more robust performance.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to enhance the functionality of this scraper.

## License

This project is licensed under the MIT License.
