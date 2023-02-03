import requests
import shutil

import os

from defisheye import Defisheye

def download_image(url, author_id):
    file_name = author_id
    response = requests.get(url, stream = True)
    if response.status_code == 200:
        with open(f'{file_name}.jpg','wb') as f:
            shutil.copyfileobj(response.raw, f)
        print(f'Image sucessfully Downloaded: {file_name}.jpg')
        return f'{file_name}.jpg'
    else:
        print('Image Couldn\'t be retrieved')

def defish(url, author_id):
    img = download_image(url, author_id)

    dtype = 'linear'
    format = 'fullframe'
    fov = 180
    pfov = 120

    img_out = f"{img}_{dtype}_{format}_{pfov}_{fov}.jpg"

    obj = Defisheye(img, dtype=dtype, format=format, fov=fov, pfov=pfov)
    obj.convert(img_out)
    os.remove(img)
    return img_out
