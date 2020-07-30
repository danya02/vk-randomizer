import requests
import random
import os
import functools
import urllib.parse
from . import temp_file
import json
import mimetypes
from . import SECRETS

sources = []
def source(minv, maxv):
    def wrapper(func):
        sources.append((func, minv, maxv))
        return func
    return wrapper

def download(url):
    with requests.get(url, stream=True) as req:
        ext = mimetypes.guess_extension(req.headers.get('content-type') or 'image/jpeg')
        file = temp_file.TemporaryFile.generate_new(ext=ext[1:])
        with open(file, 'wb') as handle:
            req.raise_for_status()
            for chunk in req.iter_content(chunk_size=8192):
                handle.write(chunk)
    return file

def download_list(urls):
    return list(map(download, urls))

@source(1,31)
def unsplash_vert(count):
    r = requests.get('https://api.unsplash.com/photos/random?client_id=' + SECRETS.unsplash_key + '&orientation=portrait&count='+str(count)).json()
#    r = json.loads(open('/tmp/res').read())
    urls = []
    for img in r:
        urls.append(img['urls']['regular'])
    return download_list(urls)


def get_any(count):
    acceptable = []
    for i in sources:
        if count in range(i[1], i[2]): 
            acceptable.append(i[0])
    if len(acceptable) == 0:
        raise ValueError(f'no acceptable image source for count: {count}')
    return random.choice(acceptable)(count)

