from random import randint
from dotenv import load_dotenv
from sources.spacex import spacex_get_last_launch_photos
from sources.nasa import nasa_get_pictures
from sources.nasa import nasa_get_epic


if __name__ == '__main__':
    load_dotenv()
    spacex_get_last_launch_photos()
    nasa_get_pictures(randint(30, 50))
    nasa_get_epic()
