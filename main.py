from dotenv import load_dotenv
import random
import os
import telegram
import time


def post_image(bot, directory, image_name):
    source = image_name.split('_')[0].upper()
    company_name = 'SpaceХ' if source == 'SPACEX' else 'NASA'
    caption = f'This photo provided by {source} API from {company_name} ' \
              f'and posted automatically for educational purposes.'

    bot.send_photo(chat_id=chat_id, photo=open(f'{directory}/{image_name}', 'rb'), caption=caption)


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
        post_image(bot, directory, images[-1])
        images.pop()
        time.sleep(delay)
