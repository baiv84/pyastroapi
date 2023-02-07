import os
import requests
import argparse
from basic import download_image, get_file_extension


def get_launch_photo_urls(launch_id):
    """Get photo URLs of launch with particular <id>"""
    api_link = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(api_link)
    response.raise_for_status()
    spacex_photo_urls = response.json()['links']['flickr']['original']
    return spacex_photo_urls


def get_last_launch_urls():
    """Get last launch photo URLs"""
    api_link = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(api_link)
    response.raise_for_status()
    launches = response.json()
    launch_database = {}

    for launch in launches:
        launch_date = launch['date_unix']
        launch_id = launch['id']
        launch_database[launch_date] = launch_id

    launch_dates = sorted(launch_database, reverse=True)
    for launch_date in launch_dates:
        launch_id = launch_database[launch_date]
        launch_photo_links = get_launch_photo_urls(launch_id)
        if len(launch_photo_links) > 0:
            return launch_photo_links
    return []


def get_spacex_photos(launch_id=None, folder='images'):
    """Download SpaceX launch photos"""
    launch_fname_prefix = ''
    try:
        if not launch_id:
            launch_photo_urls = get_last_launch_urls()
            launch_fname_prefix = 'spacex_last_launch'
        else:
            launch_photo_urls = get_launch_photo_urls(launch_id)
            launch_fname_prefix = 'spacex'
    except requests.HTTPError:
        launch_photo_urls = []

    for launch_index, launch_photo_url in enumerate(launch_photo_urls):
        launch_fname_ext = get_file_extension(launch_photo_url)
        launch_fname = f'{launch_fname_prefix}_{launch_index}{launch_fname_ext}'
        download_image(launch_photo_url, folder, launch_fname)


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
