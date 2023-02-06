import os
import time
import random
import argparse
from dotenv import load_dotenv
from astro24bot import send_photo_to_channel
from fetch_epic_images import get_epic_photos


def initialize_image_folder(images_folder, nasa_token):
    """Initialize images folder"""    
    get_epic_photos(images_folder, nasa_token)
    photos = [f'{images_folder}/{fname}' for fname in os.listdir(images_folder)]
    return photos


def main():
    """Program entry point"""
    load_dotenv()
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    # init_commands = [
    #     'python3 fetch_spacex_images.py',
    #     'python3 fetch_spacex_images.py --launch_id=5eb87ce6ffd86e000604b33a',
    #     'python3 fetch_nasa_images.py',
    #     'python3 fetch_nasa_images.py --count 10',
    #     'python3 fetch_epic_images.py',
    # ]

    images_folder = os.environ['IMAGE_FOLDER']
    nasa_token = os.environ['NASA_TOKEN']
    #telegram_token = os.environ['TELEGRAM_TOKEN']
    #update = os.environ['UPDATE_PERIOD']

    photos = []

    parser = argparse.ArgumentParser(
        description='Space photo grabber'
    )

    parser.add_argument('--period', default=4, help='Delay period in hours')
    args = parser.parse_args()
    update_period = int(args.period) * 3600

    while True:
        if len(photos) == 0:
            print('Initialize photo folder...')
            photos = initialize_image_folder(images_folder, nasa_token)
        else:
            random.shuffle(photos)
            photo = photos.pop()
            send_photo_to_channel(photo)
            time.sleep(update_period)


if __name__ == '__main__':
    main()
