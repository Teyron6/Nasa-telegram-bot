import os
import requests
from download_img import download_img
from urllib.parse import urlparse, unquote


def extract_link(url):
    decoded_link = unquote(url)
    parsed_link = urlparse(decoded_link)
    path, full_name = os.path.split(parsed_link.path)
    file_path = os.path.splitext(full_name)
    file_name, extantion = file_path
    return extantion, file_name


def get_apod_img(nasa_api_key):
    url_apod = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key' : nasa_api_key,
        'count' : 5,
    }
    response = requests.get(url_apod, params=params)
    response.raise_for_status()
    urls = response.json()

    for url in  urls:
        link = url['hdurl']
        extention,filename = extract_link(link)
        filepath = os.path.join('apod', f'{filename}{extention}')
        download_img(link, filepath)


def main():
    nasa_api_key = os.environ.get('NASA_API_KEY')
    get_apod_img(nasa_api_key)


if __name__ == '__main__':
    main()