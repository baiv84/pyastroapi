import pathlib
import requests
from dotenv import load_dotenv


IMAGE_URLS = [
    ('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'hubble.jpeg'),
    ('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'hubble2.jpeg'),
]


def download_image(url, folder, filename):
    """Download image via URL link to the folder"""
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    output = f'{folder}/{filename}'
    with open(output, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    for url, fname in IMAGE_URLS:
        download_image(url, 'images', fname)
