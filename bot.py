from dotenv import load_dotenv
import os
import telegram

if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text='This message was sent by python-telegram-bot')
