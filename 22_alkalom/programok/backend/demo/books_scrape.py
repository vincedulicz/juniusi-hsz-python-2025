import requests
from bs4 import BeautifulSoup

class BookScraper:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url

    def fetch_page(self, page_number):
        url = f'{self.base_url}/catalogue/page-{page_number}.html'
        response = self.session.get(url)

        if response.status_code != 200:
            print(f'Hiba van: {page_number} : {response.status_code}')

        return BeautifulSoup(response.content, 'html.parser')

    @staticmethod
    def extract_books(soup):
        if not soup:
            return []

        books = []

        articles = soup.find_all('article', class_='product_pod')

        for article in articles:
            title = article.h3.a['title']
            price = article.find('p', class_='price_color').text

            books.append({"title": title, "price": price})

        return books

    def scrape_all_page(self, max_pages=5):
        all_books = []

        for page in range(1, max_pages + 1):
            print(f'scraping page {page}')

            soup = self.fetch_page(page)
            books = self.extract_books(soup)

            if not books:
                break

            all_books.extend(books)

        return all_books

def main():
    base_url = "http://books.toscrape.com"
    scraper = BookScraper(base_url)
    books = scraper.scrape_all_page(max_pages=3)

    for book in books:
        print(f'{book["title"]} - {book["price"]}')

main()
