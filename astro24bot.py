import os
import random
import telegram


def send_photo_to_channel(channel_name, telegram_token, image_folder, photo=None, text=None):
    """Send photo with message to channel"""
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))
    bot = telegram.Bot(token=telegram_token)

    if text:
        bot.send_message(chat_id=channel_name, text=text)

    if not photo:
        photo_files = os.listdir(image_folder)
        photo = random.choice(photo_files)
        photo = f'{image_folder}/{photo}'

    print(f'\n************************************\nSending file  - {photo}')
    with open(photo, 'rb') as photo_file:
        bot.send_document(chat_id=channel_name, document=photo_file)
