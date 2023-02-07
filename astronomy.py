import os
import time
import random
import argparse
from dotenv import load_dotenv
from astro24bot import send_photo_to_channel
from fetch_nasa_images import get_nasa_photos
from fetch_epic_images import get_epic_photos
from fetch_spacex_images import get_spacex_photos


def initialize_image_folder(nasa_token, image_folder):
    """Initialize images folder"""
    get_spacex_photos()
    get_nasa_photos(nasa_token=nasa_token, folder=image_folder)
    get_nasa_photos(nasa_token=nasa_token, folder=image_folder, count=10)
    get_epic_photos(nasa_token=nasa_token, folder=image_folder)

    astro_photos = [f'{image_folder}/{fname}' for fname in os.listdir(image_folder)]
    return astro_photos


def main():
    """Program entry point"""
    load_dotenv()
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    try:
        image_folder = os.environ['IMAGE_FOLDER']
        nasa_token = os.environ['NASA_TOKEN']
        telegram_token = os.environ['TELEGRAM_TOKEN']
        update_period = os.environ['UPDATE_PERIOD']
        chat_id = os.environ['CHAT_ID']
    except KeyError:
        print('\n*******************************\n'
              'Error loading program settings.\n'
              'Check .env file for correctness\n')
        return

    astro_photos = []

    parser = argparse.ArgumentParser(
        description='Space photo grabber'
    )

    parser.add_argument('--period', default=4, help='Delay period in hours')
    args = parser.parse_args()
    update_period = int(args.period) * 3600

    while True:
        if len(astro_photos) == 0:
            print('Initialize photo folder...')
            astro_photos = initialize_image_folder(nasa_token, image_folder)
        else:
            random.shuffle(astro_photos)
            astro_photo = astro_photos.pop()
            send_photo_to_channel(chat_id, telegram_token, image_folder, astro_photo)
            print('\n************************************')
            print('Waiting for the next start...')
            time.sleep(update_period)


if __name__ == '__main__':
    main()
