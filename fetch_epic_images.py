import os
import requests
import argparse
from basic import download_image


def get_epic_photos(nasa_token, folder='images'):
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
        epic_link = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_identifier}.png'
        filename = f'nasa_epic_{i}.png'
        download_image(epic_link, folder, filename, params={'api_key': nasa_token})


def main():
    """Program entry point"""
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    parser = argparse.ArgumentParser(
        description='Space photo grabber'
    )

    parser.add_argument('--nasa_token')
    parser.add_argument('--folder', default='images')
    args = parser.parse_args()
    get_epic_photos(args.nasa_token, args.folder)


if __name__ == '__main__':
    main()
