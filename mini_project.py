import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string
    else:
        return "Error: Unable to retrieve the page"

def main():
    url = input("Enter the URL of the page to scrape: ")
    print(f"Page title: {get_page_title(url)}")

if __name__ == "__main__":
    main()
