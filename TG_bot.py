import telegram
import random
import os
from os import listdir
from time import sleep
from dotenv import load_dotenv


def bot(tg_token, tg_chat_id, sleep_time):
    bot = telegram.Bot(tg_token)
    while True:
        folder = 'images'
        files = listdir(folder)
        file = random.choice(files)
        path = os.path.join(folder, file)
        with open(path, 'rb') as f:
            bot.send_document(tg_chat_id, document=f)
        sleep(sleep_time)


def main():
    load_dotenv()
    tg_token = os.environ.get('TG_TOKEN')
    tg_chat_id = os.environ.get('TG_CHAT_ID')
    sleep_time = int(os.environ.get('SLEEP_TIME', 14400))
    bot(tg_token, tg_chat_id, sleep_time)



if __name__ == '__main__':
    main()