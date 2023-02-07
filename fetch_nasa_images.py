import os
import requests
import argparse
from basic import download_image, get_file_extension


def get_nasa_photos(nasa_token, folder='images', count=None):
    """Download <count> NASA photos of the day"""
    if not nasa_token:
        print('Token is not set')
        return

    apod_url = f'https://api.nasa.gov/planetary/apod/'
    response = requests.get(
        apod_url,
        params={'api_key': nasa_token, 'count': count}
    )

    response.raise_for_status()
    apod_photos = response.json()

    if not count:
        apod_photo_url = apod_photos['url']
        download_image(apod_photo_url, folder, 'apod.jpg')
    else:
        apod_photo_urls = [apod_photo['url'] for apod_photo in apod_photos if apod_photo['media_type'] == 'image']
        for index, apod_photo_url in enumerate(apod_photo_urls):
            apod_file_ext = get_file_extension(apod_photo_url)
            apod_file_name = f'nasa_apod_{index}{apod_file_ext}'
            download_image(apod_photo_url, folder, apod_file_name)


def main():
    """Program entry point"""
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    parser = argparse.ArgumentParser(
        description='Space photo grabber'
    )

    parser.add_argument('--nasa_token')
    parser.add_argument('--folder', default='images')
    parser.add_argument('--count')
    args = parser.parse_args()
    get_nasa_photos(args.nasa_token, args.folder, args.count)


if __name__ == '__main__':
    main()
