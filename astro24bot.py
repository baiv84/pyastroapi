import os
import telegram
from dotenv import load_dotenv

def send_photo_to_channel(photo, text):
    """Send photo with message to channel"""
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)
    bot.send_message(chat_id='@astro24channel', text=text)
    bot.send_document(chat_id='@astro24channel', document=open(photo, 'rb'))
