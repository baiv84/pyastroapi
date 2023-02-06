import os
import requests
import argparse
from dotenv import load_dotenv
from basic import download_image


def get_epic_photos(image_folder='images',nasa_token=None):
    """Download EPIC photos"""
    if not nasa_token:
        print('Token is not set')
        return

    epic_url = f'https://api.nasa.gov/EPIC/api/natural/images/'
    response = requests.get(epic_url, params={'api_key': nasa_token})
    response.raise_for_status()
    epics = response.json()

    for i, epic in enumerate(epics):
        photo_identifier = epic['image']
        photo_date, _ = epic['date'].split()
        photo_date = photo_date.replace('-', '/')
        epic_link = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_identifier}.png?api_key={nasa_token}'

        file_name = f'nasa_epic_{i}.png'
        download_image(epic_link, image_folder, file_name, 'Grabbing EPIC')


def main():
    """Program entry point"""
    #load_dotenv()
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    parser = argparse.ArgumentParser(
        description='Space photo grabber'
    )

    parser.add_argument('--token')
    parser.add_argument('--folder', default='images')
    args = parser.parse_args()
    get_epic_photos(args.folder, args.token)


if __name__ == '__main__':
    main()
