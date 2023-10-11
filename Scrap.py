import requests
from bs4 import BeautifulSoup

def scrape_wallpapers(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        image_tags = soup.find_all('img', class_='wp-image')

        image_urls = [img['src'] for img in image_tags]
        
        return image_urls
    else:
        print(f'Error: Unable to fetch content. Status code: {response.status_code}')
        return None

if __name__ == '__main__':
    url = 'https://wallpapercave.com/aggretsuko-wallpapers'
    image_urls = scrape_wallpapers(url)

    if image_urls:
        for i, url in enumerate(image_urls, 1):
            print(f"Image {i}: {url}")
