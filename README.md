# Telegram space images

This program fetches space photos and uploads them to telegram channel.

### How to install

Create an `.env` file in the project directory. Create a new telegram bot through a BotFather and assign its token to `TELEGRAM_BOT_TOKEN` variable. Create an account on NASA website and generate token to use its API, assign it to `NASA_API_KEY` variable. Assign your telegram channel ID to `TELEGRAM_CHAT_ID` variable. You can also set `DELAY` variable to adjust time between posts, which is 14400 seconds (4 hours) by default.

Example of an `.env` file:

```
TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
TELEGRAM_CHAT_ID="@chatid"
NASA_API_KEY="YOUR_KEY"
DELAY="14400"
```

Python3 should already be installed. Use pip (or pip3, in case of conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Usage

To run the programm use the following command from the project directory:
```
python main.py
```
To download images from SpaceX use the following command from the project directory:
```
python fetch_spacex_images.py launch_id
```
Latest launch photos will be downloaded if *launch_id* is not set.

To download images from NASA use the one of following commands:
```
python fetch_nasa_apod_images.py

python fetch_nasa_epic_images.py
```
Don't forget to set your NASA API KEY.
### Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).