import os
import requests
import argparse
from datetime import datetime
from basic import download_image


def get_launch_photo_urls(launch_id):
    """Get photo URLs of launch with particular <id>"""
    api_link = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(api_link)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    return photo_urls


def get_last_launch_urls():
    """Get last launch photo URLs"""
    api_link = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(api_link)
    response.raise_for_status()
    launches = response.json()
    launch_info = {}

    for launch in launches:
        launch_date = launch['date_unix']
        launch_id = launch['id']
        launch_info[launch_date] = launch_id

    launch_dates = sorted(launch_info, reverse=True)
    for date in launch_dates:
        launch_id = launch_info[date]
        photo_links = get_launch_photo_urls(launch_id)
        if len(photo_links) > 0:
            return photo_links
    return []


def get_spacex_photos(launch_id=None, folder='images'):
    """Download SpaceX launch photos"""
    try:
        if not launch_id:
            photo_urls = get_last_launch_urls()
        else:
            photo_urls = get_launch_photo_urls(launch_id)
    except requests.HTTPError:
        photo_urls = []

    for i, url in enumerate(photo_urls):
        filename = f'spacex_{i}.jpg'
        download_image(url, folder, filename)



def main():
    """Program entry point"""
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))
  
    parser = argparse.ArgumentParser(
        description='Space photo grabber'
    )

    parser.add_argument('--launch_id')
    args = parser.parse_args()
    get_spacex_photos(args.launch_id)


if __name__ == '__main__':
    main()
