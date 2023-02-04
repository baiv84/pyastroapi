import requests
from datetime import datetime
from common.basicfunc import download_image


def get_photo_urls(id_launch):
    """Get photo URLs of launch with particular <id>"""
    api_link = f'https://api.spacexdata.com/v5/launches/{id_launch}'
    response = requests.get(api_link)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    return photo_urls


def fetch_spacex_last_launch():
    """Return last launch photo URLs"""
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
        readable_launch_date = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
        id_launch = launch_info[date]
        photo_links = get_photo_urls(id_launch)
        print(f'Parse launch with id - {id_launch}, date - {readable_launch_date}')
        if len(photo_links) > 0:
            print(f'Last launch with photos date - {readable_launch_date}')
            print(f'Last launch with photos id - {id_launch}')
            return photo_links
    return []


def spacex_get_last_launch_photos():
    """Download last launch photos"""
    photo_urls = fetch_spacex_last_launch()
    for i, url in enumerate(photo_urls):
        file_name = f'spacex_{i}.jpg'
        download_image(url, file_name)