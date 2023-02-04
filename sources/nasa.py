import os
import requests
from common.basicfunc import download_image


def nasa_get_picture_of_day():
    """Download NASA picture of the day"""
    nasa_token = os.environ['NASA_TOKEN']
    nasa_apod_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_token}'

    response = requests.get(nasa_apod_url)
    response.raise_for_status()

    apod_url = response.json()['url']
    download_image(apod_url, 'apod.jpg')
