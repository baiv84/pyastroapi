from dotenv import load_dotenv
from sources.spacex import spacex_get_last_launch_photos
from sources.nasa import nasa_get_picture_of_day


if __name__ == '__main__':
    load_dotenv()
    spacex_get_last_launch_photos()
    nasa_get_picture_of_day()
