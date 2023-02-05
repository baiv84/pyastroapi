import os
import random
import telegram
from dotenv import load_dotenv


def send_photo_to_channel(photo=None, text=None):
    """Send photo with message to channel"""
    load_dotenv()
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))

    image_folder = os.environ['IMAGE_FOLDER']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)

    if text:
        bot.send_message(chat_id='@astro24channel', text=text)

    if not photo:
        photos = os.listdir(image_folder)
        photo = random.choice(photos)
        photo = f'{image_folder}/{photo}'

    bot.send_document(chat_id='@astro24channel', document=open(photo, 'rb'))
