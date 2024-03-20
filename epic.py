import os
import requests
import datetime
from download_img import download_img
from dotenv import load_dotenv


def get_epic_img(nasa_api_key):
    url_epic = 'https://api.nasa.gov/EPIC/api/natural/image'
    params = {
        'api_key' : nasa_api_key,
    }
    response = requests.get(url_epic, params=params)
    response.raise_for_status()
    urls = response.json()
    for url in urls:
        epic_date = url['date']
        epic_date = datetime.datetime.fromisoformat(epic_date).strftime('%Y/%m/%d')
        epic_img = url['image']
        epic_link = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_img}.png'
        path = os.path.join('epic', f'{epic_img}.png')
        download_img(epic_link, path, params)


def main():
    load_dotenv()
    nasa_api_key = os.environ.get('NASA_API_KEY',)
    get_epic_img(nasa_api_key)


if __name__ == '__main__':
    main()
