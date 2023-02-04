import os
import requests
import argparse
from dotenv import load_dotenv
from basic import download_image, get_file_extension


def nasa_get_photos(count=None):
    """Download <count> NASA photos of the day"""
    nasa_token = os.environ['NASA_TOKEN']
    apod_url = f'https://api.nasa.gov/planetary/apod/'

    response = requests.get(apod_url, params={'api_key': nasa_token, 'count': count})
    response.raise_for_status()
    apods = response.json()

    if count:
        photos = [apod['url'] for apod in apods if apod['media_type'] != 'video']
        for i, photo in enumerate(photos):
            ext = get_file_extension(photo)
            file_name = f'nasa_apod_{i}{ext}'
            download_image(photo, 'NASA_FOLDER', file_name, 'Grabbing NASA')
    else:
        photo = apods['url']
        download_image(photo, 'NASA_FOLDER', 'apod.jpg', 'Grabbing NASA')


load_dotenv()
parser = argparse.ArgumentParser(
    description='Space photo grabber'
)

parser.add_argument('--count', help='Photo count')
args = parser.parse_args()
nasa_get_photos(args.count)
