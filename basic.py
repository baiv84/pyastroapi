import os
import pathlib
import requests
from urllib.parse import urlsplit, unquote


def download_image(url, folder, filename, params={}):
    """Download image via URL link to the folder"""
    print(f'Download file - {filename}')
    response = requests.get(url, params=params)
    response.raise_for_status()

    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    full_path = f'{folder}/{filename}'
    with open(full_path, 'wb') as file:
        file.write(response.content)


def get_file_name(url):
    """Extract file name from URL"""
    file_path = urlsplit(url).path
    file_path = unquote(file_path)
    _, file_name = os.path.split(file_path)
    return file_name


def get_file_extension(url):
    """Extract file extension from URL"""
    file_path = urlsplit(url).path
    file_path = unquote(file_path)
    _, file_ext = os.path.splitext(file_path)
    return file_ext
