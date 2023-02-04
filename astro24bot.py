import os
import telegram
from dotenv import load_dotenv


load_dotenv()

telegram_token = os.environ['TELEGRAM_TOKEN']
bot = telegram.Bot(token=telegram_token)
bot.send_message(chat_id='@astro24channel', text="Привет всем!")
