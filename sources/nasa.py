import os
import requests
from common.basicfunc import download_image, get_file_extension


def nasa_get_pictures(count=None):
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


def nasa_get_epic():
    """Download EPIC pictures"""
    nasa_token = os.environ['NASA_TOKEN']
    epic_url = f'https://api.nasa.gov/EPIC/api/natural/images/'

    response = requests.get(epic_url, params={'api_key': nasa_token})
    response.raise_for_status()
    epics = response.json()

    for i, epic in enumerate(epics):
        photo_identifier = epic['image']
        photo_date, _ = epic['date'].split()
        photo_date = photo_date.replace('-', '/')
        epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_identifier}.png?api_key=Q8XtfftJgPfexGIjh8MZ1MBFKC0umQiuutWSUHCV"

        file_name = f'nasa_epic_{i}.png'
        download_image(epic_link, 'NASA_EPIC', file_name, 'Grabbing EPIC')
