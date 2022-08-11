from dotenv import load_dotenv
import random
import os
import telegram
import time
from pathlib import Path


def post_image(bot, directory, image_name):
    source = image_name.split('_')[0].upper()
    company_name = 'SpaceХ' if source == 'SPACEX' else 'NASA'
    caption = f'This photo provided by {source} API from {company_name} ' \
              f'and posted automatically for educational purposes.'

    with open(Path(f'{directory}/{image_name}'), 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)


if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    directory = 'images'
    images = []
    delay = int(os.getenv('DELAY', 14400))

    bot = telegram.Bot(token=token)

    while True:
        if not images:
            images = os.listdir(directory)
            random.shuffle(images)
        post_image(bot, directory, images.pop())
        time.sleep(delay)
