import requests
from bs4 import BeautifulSoup

url = 'https://wallpapercave.com/aggretsuko-wallpapers'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the image URLs from the HTML
image_urls = []
for image in soup.find_all('img', class_='wallpaper-image'):
    image_urls.append(image['src'])

# Save the image URLs to a file
with open('aggretsuko_wallpapers.txt', 'w') as f:
    for image_url in image_urls:
        f.write(image_url + '\n')

# Print the number of image URLs that were scraped
print('The number of image URLs that were scraped is:', len(image_urls))
