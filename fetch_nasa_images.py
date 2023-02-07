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
    apods = response.json()
    
    if not count:
        photo_url = apods['url']
        download_image(photo_url, folder, 'apod.jpg')
    else:
        photo_urls = [apod['url'] for apod in apods if apod['media_type'] == 'image']
        for i, photo_url in enumerate(photo_urls):
            ext = get_file_extension(photo_url)
            filename = f'nasa_apod_{i}{ext}'
            download_image(photo_url, folder, filename)
    

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
