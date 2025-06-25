import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_products(page=1):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    products = []

    for item in soup.select('article.product_pod'):
        title = item.h3.a['title']
        price = item.select_one('p.price_color').text.strip().lstrip('£')
        stock = item.select_one('p.instock').text.strip()
        products.append({
            'title': title,
            'price_gbp': float(price),
            'stock_text': stock,
            'stock_binary': 0 if 'In stock' in stock else 1,
            'timestamp': datetime.now()
        })
    return pd.DataFrame(products)

# Scrape first 3 pages
df = pd.concat([scrape_products(i) for i in range(1, 51)], ignore_index=True)
df.to_csv("scraped_data.csv", index=False)
print(f"Scraped {len(df)} books.")
