import datetime
import os
from dotenv import load_dotenv
import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote


def download_image(url, path, image_name, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{path}/{image_name}', 'wb') as file:
        file.write(response.content)


def get_extension_from_url(url):
    path = Path(urlsplit(unquote(url)).path)
    extension = path.suffix
    return extension


def fetch_spacex_last_lauch():
    spacex_api_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'

    response = requests.get(spacex_api_url)
    response.raise_for_status()

    spacex_image_urls = response.json()['links']['flickr']['original']
    for index, url in enumerate(spacex_image_urls, start=1):
        image_name = f'spacex_{index}{get_extension_from_url(url)}'
        download_image(url, 'images', image_name)


def fetch_nasa_apod(count=10):
    nasa_apod_api_url = 'https://api.nasa.gov/planetary/apod'
    apod_paylaod = {'count': count, 'api_key': NASA_API_KEY}

    response = requests.get(nasa_apod_api_url, params=apod_paylaod)
    response.raise_for_status()

    apod_urls = [element['url'] for element in response.json()]
    for index, url in enumerate(apod_urls, start=1):
        image_name = f'apod_{index}{get_extension_from_url(url)}'
        download_image(url, 'images', image_name)


def fetch_nasa_epic():
    nasa_epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    epic_payload = {'api_key': NASA_API_KEY}

    response = requests.get(nasa_epic_api_url, params=epic_payload)
    response.raise_for_status()

    for index, image_metadata in enumerate(response.json(), start=1):
        image_date = datetime.datetime.fromisoformat(image_metadata['date'])
        image_name = image_metadata['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date:%Y/%m/%d}/png/{image_name}.png'
        downloaded_image_name = f'epic_{index}.png'
        download_image(image_url, 'images', downloaded_image_name, payload=epic_payload)


if __name__ == '__main__':
    load_dotenv()
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    fetch_spacex_last_lauch()
    fetch_nasa_apod()
    fetch_nasa_epic()
