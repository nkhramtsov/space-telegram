from dotenv import load_dotenv
import os
import telegram

if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    bot = telegram.Bot(token=token)

    caption = 'This photo provided by bot for educational purposes'
    bot.send_photo(chat_id=chat_id, photo=open('images/epic_1.png', 'rb'), caption=caption)
