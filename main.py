import pathlib
import requests
from dotenv import load_dotenv

FOLDER = 'images'
pathlib.Path(FOLDER).mkdir(parents=True, exist_ok=True)

IMAGE_URLS = [
    ('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'hubble.jpeg'),
    ('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'hubble2.jpeg'),
]


def download_image(url, filename):
    """Download image via URL link to the folder"""
    response = requests.get(url)
    response.raise_for_status()

    full_path = f'{FOLDER}/{filename}'
    with open(full_path, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    for url, fname in IMAGE_URLS:
        download_image(url, fname)
