import requests
from download_img import download_img
import random
import argparse


def fetch_spacex_last_launch(launch_id):
    link = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(link)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    for url_num, url in enumerate(urls):
        path = f'spacex/spacex_{url_num}.jpeg'
        download_img(url, path)


def main():
    parser = argparse.ArgumentParser(
        description='Эта программа позволит вам загрузить фотографии с запуска SpaceX.'
    )
    parser.add_argument(
        '--id',
        dest='launch_id',
        default='5eb87d47ffd86e000604b38a',
        help='Укажите ID запуска SpaceX, с которого можно загрузить фотографии.'
    )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == '__main__':
    main()