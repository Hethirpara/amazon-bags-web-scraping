import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

product_urls = []
product_names = []
product_prices = []
ratings = []
review_counts = []

for page in range(1, 21):  # Scrape 20 pages
    url = f"https://www.amazon.in/s?k=bags&page={page}&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    for product in products:
        try:
            product_url = "https://www.amazon.in" + product.find('a', {'class': 'a-link-normal'})['href']
            product_urls.append(product_url)
        except Exception as e:
            product_urls.append('N/A')

        try:
            product_name_element = product.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).find('span',{'class':'a-size-medium a-color-base a-text-normal'})
            product_name = product_name_element.text if product_name_element else 'N/A'
            product_names.append(product_name)
        except Exception as e:
            product_names.append('N/A')

        try:
            product_price_element = product.find('span', {'class': 'a-offscreen'})
            product_price = product_price_element.text if product_price_element else 'N/A'
            product_prices.append(product_price)
        except Exception as e:
            product_prices.append('N/A')

        try:
            rating_element = product.find('span', {'class': 'a-icon-alt'})
            rating = rating_element.text if rating_element else 'N/A'
            ratings.append(rating)
        except Exception as e:
            ratings.append('N/A')

        try:
            review_count_element = product.find('span', {'class': 'a-size-base s-underline-text'})
            review_count = review_count_element.text if review_count_element else 'N/A'
            review_counts.append(int(review_count.replace(',', '')))
        except Exception as e:
            review_counts.append('N/A')

    # Add a delay to prevent getting blocked by Amazon
    time.sleep(2)

data = {
    'Product URL': product_urls,
    'Product Name': product_names,
    'Product Price': product_prices,
    'Rating': ratings,
    'Number of Reviews': review_counts
}

df = pd.DataFrame(data)

# Exporting DataFrame to CSV
df.to_csv('scraped_data.csv', index=False)

print("Scraping completed and data saved to 'scraped_data.csv'")
