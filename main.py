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
    # for command in COMMANDS:
    #     os.system(command)
    
    send_photo_to_channel('images/nasa_epic_0.png', ' Планета Земля!')
