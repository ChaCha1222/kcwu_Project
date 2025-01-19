import requests
from bs4 import BeautifulSoup

url = 'https://www.klook.com/zh-TW/activity/8875-chimei-museum-permanent-exhibition-ticket-tainan/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Save the scraped content to a file
with open('scraped_content.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())