import os
import requests
from dotenv import load_dotenv
from basic import download_image


def get_epic_photos():
    """Download EPIC photos"""
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


load_dotenv()
get_epic_photos()
