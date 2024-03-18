import requests
from download_img import download_img


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    n = 1
    for i in urls:
        filename = f'spacex/spacex_{n}.jpeg'
        url = i
        n += 1
        download_img(url, filename)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()