import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
import time
import random
import pandas as pd
from fake_useragent import UserAgent

# Initialize global variables
reviewss = []
currentPage = [1]
totalPages = 55

# Function to switch Tor identity
def switch_tor_identity():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # Replace with your actual password
        controller.signal(Signal.NEWNYM)

# Function to make a request using Tor
def get_page(url):
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    headers = {
        'User-Agent': UserAgent().random,
    }
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

# Scraping function
def scrape_amazon_reviews(product_url, currentPage, totalPages, reviewss):
    response = get_page(product_url)
    if response is None or response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code if response else 'No response'}")
        return None, reviewss

    soup = BeautifulSoup(response.content, 'html.parser')
    reviews = soup.find_all('div', {'data-hook': 'review'})

    for review in reviews:
        title = review.find('a', {'data-hook': 'review-title'})
        rating = review.find('i', {'data-hook': 'review-star-rating'})
        text = review.find('span', {'data-hook': 'review-body'})

        title = title.text.strip() if title else "No Title"
        rating = rating.text.strip() if rating else "No Rating"
        text = text.text.strip() if text else "No Review Text"

        reviewss.append({
            'title': title,
            'rating': rating,
            'review': text
        })

    if currentPage[0] < totalPages:
        currentPage[0] += 1
        next_page_url = f"{product_url}?pageNumber={str(currentPage[0])}"
        print(next_page_url)
        return next_page_url, reviewss
    return None, reviewss

# Main script to scrape multiple pages
def main(product_url, currentPage, totalPages, reviewss):
    while product_url:
        product_url, reviewss = scrape_amazon_reviews(product_url, currentPage, totalPages, reviewss)
        if product_url:
            print(f"Next page: {product_url}")
        delay = random.uniform(10, 20)  # Random delay between 10 and 20 seconds
        time.sleep(delay)
        switch_tor_identity()  # Change IP address

# Replace with the actual product URL
product_url = 'https://www.amazon.in/i7-14700K-Desktop-Processor-Integrated-Graphics/product-reviews/B0CGJ41C9W/ref=sr_1_1'

main(product_url, currentPage, totalPages, reviewss)

# Save reviews to CSV
df = pd.DataFrame(reviewss)
df.to_csv('amazon_reviews.csv', index=False)
