import telegram
import random
import os
from os import listdir
from time import sleep
from dotenv import load_dotenv


def bot():
    bot = telegram.Bot(os.environ.get('TG_TOKEN'))
    while True:
        folders = ['spacex', 'apod', 'epic']
        folder = random.choice(folders)
        files = listdir(folder)
        random.shuffle(files)
        for file in files:
            path = os.path.join(folder, file)
            with open(path, 'rb') as f:
                bot.send_document(os.environ.get('TG_CHAT_ID'), document=f)
            sleep(int(os.environ.get('SLEEP_TIME', 14400)))


def main():
    load_dotenv()
    bot()



if __name__ == '__main__':
    main()