import datetime
from dotenv import load_dotenv
import requests
import os
from utils import download_image


def fetch_nasa_epic():
    nasa_epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    epic_payload = {'api_key': nasa_api_key}

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
    nasa_api_key = os.getenv('NASA_API_KEY')
    fetch_nasa_epic()
