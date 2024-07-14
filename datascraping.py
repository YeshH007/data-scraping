import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_data(soup):
    data = []
    items = soup.find_all('div', class_='item')
    for item in items:
        title = item.find('h2').text
        data.append(title)
    return data

def filter_data(data):
    return list(filter(lambda x: 'Python' in x, data))

def display_data(data):
    print(f"Total items: {len(data)}")
    for item in data:
        print(item)

url = 'https://example.com'
html = fetch_html(url)
soup = parse_html(html)
data = extract_data(soup)
filtered_data = filter_data(data)
display_data(filtered_data)
