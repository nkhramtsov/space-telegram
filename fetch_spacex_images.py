import argparse
import requests
from utils import download_image, get_extension_from_url


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', type=str)

    return parser.parse_args()


def fetch_spacex_launch(launch_id='latest'):
    spacex_api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(spacex_api_url)
    response.raise_for_status()

    spacex_image_urls = response.json()['links']['flickr']['original']
    for index, url in enumerate(spacex_image_urls, start=1):
        image_name = f'spacex_{index}{get_extension_from_url(url)}'
        download_image(url, 'images', image_name)


if __name__ == '__main__':
    arguments = parse_args()
    fetch_spacex_launch(arguments.launch_id)
