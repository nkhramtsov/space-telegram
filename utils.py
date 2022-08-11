import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote


def download_image(url, path, image_name, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    Path(path).mkdir(parents=True, exist_ok=True)
    with open(Path(f'{path}/{image_name}'), 'wb') as file:
        file.write(response.content)


def get_extension_from_url(url):
    path = Path(urlsplit(unquote(url)).path)
    extension = path.suffix
    return extension
