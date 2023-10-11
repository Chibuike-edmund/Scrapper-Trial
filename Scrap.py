import requests
from bs4 import BeautifulSoup

url = 'https://wallpapercave.com/aggretsuko-wallpapers'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data you want to scrape from the HTML
title = soup.find('title').text
description = soup.find('meta', property='description')['content']

# Print the scraped data
print(title)
print(description)
