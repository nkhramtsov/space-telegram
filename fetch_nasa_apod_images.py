from dotenv import load_dotenv
import requests
import os
from utils import download_image, get_extension_from_url


def fetch_nasa_apod(nasa_api_key, count=10):
    nasa_apod_api_url = 'https://api.nasa.gov/planetary/apod'
    apod_paylaod = {'count': count, 'api_key': nasa_api_key}

    response = requests.get(nasa_apod_api_url, params=apod_paylaod)
    response.raise_for_status()

    apod_urls = [element['url'] for element in response.json()]
    for index, url in enumerate(apod_urls, start=1):
        image_name = f'apod_{index}{get_extension_from_url(url)}'
        download_image(url, 'images', image_name)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    fetch_nasa_apod(nasa_api_key)
