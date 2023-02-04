import os
from astro24bot import send_photo_to_channel

COMMANDS = [
    'python3 fetch_spacex_images.py',
    'python3 fetch_spacex_images.py --launch_id=6243adcaaf52800c6e919254',
    'python3 fetch_nasa_images.py',
    'python3 fetch_nasa_images.py --count 10',
    'python3 fetch_epic_images.py',
]


if __name__ == '__main__':
    send_photo_to_channel('photos_nasa/nasa_apod_8.gif', 'Фото дня')
    # for command in COMMANDS:
    #     os.system(command)
