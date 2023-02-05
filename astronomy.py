import os
import time
import random
import argparse
from dotenv import load_dotenv
from astro24bot import send_photo_to_channel


load_dotenv()


INIT_COMMANDS = [
    'python3 fetch_spacex_images.py',
    'python3 fetch_spacex_images.py --launch_id=5eb87ce6ffd86e000604b33a',
    'python3 fetch_nasa_images.py',
    'python3 fetch_nasa_images.py --count 10',
    'python3 fetch_epic_images.py',
]


IMAGES_FOLDER = os.environ['IMAGE_FOLDER']


PHOTOS = []


parser = argparse.ArgumentParser(
    description='Space photo grabber'
)
parser.add_argument('--period', help='Delay period in hours')
args = parser.parse_args()

if not args.period:
    print('Use default time delay')
    UPDATE_PERIOD = int(os.environ['UPDATE_PERIOD']) * 3600
else:
    print('Use custom time delay')
    UPDATE_PERIOD = int(args.period) * 3600


def initialize_image_folder():
    """Initialize images folder"""
    global PHOTOS
    global INIT_COMMANDS
    global IMAGES_FOLDER

    for cmd in INIT_COMMANDS:
        os.system(cmd)
    PHOTOS = [f'{IMAGES_FOLDER}/{fname}' for fname in os.listdir(IMAGES_FOLDER)]


while True:
    if len(PHOTOS) == 0:
        print("Initialize photo folder...")
        initialize_image_folder()
    else:
        random.shuffle(PHOTOS)
        photo = PHOTOS.pop()
        send_photo_to_channel(photo)
        time.sleep(UPDATE_PERIOD)
