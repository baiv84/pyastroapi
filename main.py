import requests
from dotenv import load_dotenv


IMAGE_URLS = [
    ('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'hubble.jpeg'),
]


def download_image(url, filename):
    """Download image via URL link"""
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    for url, fname in IMAGE_URLS:
        download_image(url, fname)
