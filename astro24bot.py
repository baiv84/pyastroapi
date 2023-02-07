import os
import random
import telegram


def send_photo_to_channel(chat_id, telegram_token, image_folder,
                          photo_file=None, text=None):
    """Send photo with message to telegram channel"""
    absFilePath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(absFilePath))
    bot = telegram.Bot(token=telegram_token)

    if text:
        bot.send_message(chat_id=chat_id, text=text)
    if not photo_file:
        photo_files = os.listdir(image_folder)
        photo_file = random.choice(photo_files)
        photo_file = f'{image_folder}/{photo_file}'

    print(f'\n************************************\nSending file  - {photo_file}')
    with open(photo_file, 'rb') as photo_file_context:
        bot.send_document(chat_id=chat_id, document=photo_file_context)
