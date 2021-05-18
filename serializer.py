import os
from PIL import Image


def serialize(images_path=None):
    images_path = '/home/casper/Desktop/Vidrone/images'
    images_list = os.listdir(images_path)
    with open('results.txt', 'w+') as f:
        for image in images_list:
            image_row = image[19:].lstrip('0').replace('.jpg', '')
            im = Image.open(f'{images_path}/{image}')
            width, height = im.size
            f.write(f"{image_row},{width},{height}\n")
    f.close()

