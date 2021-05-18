import os
import shutil
from PIL import Image
import json
from serializer import serialize
from chcker import check

data = {
    "info": {
        "year": "2021",
        "version": "1.0",
        "description": "Exported from Visdrones",
        "contributor": "Casper",
        "url": "https://VisDrones.net",
        "date_created": "2021-01-19T09:48:27"
    },
    "licenses": [
        {
            "url": "http://MIT.net",
            "id": 1,
            "name": "MIT License"
        },
    ],
    "categories": [

        {

        },
    ],
    "images": [
        {

        },
    ],
    "annotations": [
        {

        },
    ]
}


def process(value):
    if value == '0':
        return '‫ignored regions'
    elif value == '1':
        return '‪pedestrain‬‬'
    elif value == '2':
        return 'people'
    elif value == '3':
        return '‫‪bicycle‬‬'
    elif value == '4':
        return 'car'
    elif value == '5':
        return 'van'
    elif value == '6':
        return 'truck'
    elif value == '7':
        return 'tricycle'
    elif value == '8':
        return '‫‪awning-tricycle'
    elif value == '9':
        return 'bus'
    elif value == '10':
        return 'motor'
    elif value == '11':
        return 'others'


def return_super(instance):
    if instance == 'people' or '‪pedestrain‬‬':
        return '‫Human‬‬'
    elif instance == 'car' or 'bus' or 'motor' or 'van' or 'tricycle' or '‫‪awning-tricycle' or '‫‪bicycle‬‬':
        return 'Vichle'
    elif instance == 'ignored regions':
        return 'Ignored Regions'
    else:
        return 'Others'


def combine_to_dir_train(path=None, new_path=None):
    path = '/home/casper/Desktop/Vidrone/VisDrone2019-MOT-train/sequences'
    new_path = '/home/casper/Desktop/Vidrone/images'
    content = os.listdir(path)
    for folder in content:
        images = os.listdir(f'{path}/{folder}')
        for image in images:
            new_image = f'{folder}{image}'
            shutil.move(f'{path}/{folder}/{image}', f'{new_path}/{new_image}')

def combine_to_dir_test(path=None, new_path=None):
    path = '/home/casper/Desktop/Vidrone/VisDrone2019-MOT-train/sequences'
    new_path = '/home/casper/Desktop/Vidrone/images'
    content = os.listdir(path)
    for folder in content:
        images = os.listdir(f'{path}/{folder}')
        for image in images:
            new_image = f'{folder}{image}'
            shutil.move(f'{path}/{folder}/{image}', f'{new_path}/{new_image}')

def combine_to_dir_validation(path=None, new_path=None):
    path = '/home/casper/Desktop/Vidrone/VisDrone2019-MOT-train/sequences'
    new_path = '/home/casper/Desktop/Vidrone/images'
    content = os.listdir(path)
    for folder in content:
        images = os.listdir(f'{path}/{folder}')
        for image in images:
            new_image = f'{folder}{image}'
            shutil.move(f'{path}/{folder}/{image}', f'{new_path}/{new_image}')


def make_coco(images_path=None, annotations_path=None):
    images_path = '/home/casper/Desktop/Vidrone/images'
    annotations_path = '/home/casper/Desktop/Vidrone/VisDrone2019-MOT-train/annotations'
    annotations_list = os.listdir(annotations_path)
    images_list = os.listdir(images_path)
    with open('results.txt', 'r') as f:
        results = f.read().split('\n')
    for annotation in annotations_list:
        annotation_file = open(f'{annotations_path}/{annotation}', 'r')
        lines_pre = annotation_file.read()
        lines = lines_pre.split('\n')
        for image in images_list:
            if image[:18] == annotation[:18]:
                # im = Image.open(f'{images_path}/{image}')
                image_row = image[19:].lstrip('0').replace('.jpg', '')
                for result in results:
                    result_sample = result.split(',')
                    if image_row == result_sample[0]:
                        width, height = int(result_sample[1]), int(result_sample[2])
                # ss = lines
                for line in lines:
                    line = line.split(',')
                    if line[0] == image_row:
                        if line[6] == 0:
                            continue
                        else:
                            target_id = line[1]
                            bboxes = [line[2], line[3], line[4], line[5]]
                            category = line[7]
                            data["images"].append({
                                "id": image_row,
                                "license": 1,
                                "file_name": f'{images_path}/{image}',
                                "height": height,
                                "width": width,
                                "date_captured": None
                            })
                            data["annotations"].append({
                                "id": target_id,
                                "image_id": image_row,
                                "category_id": None,
                                "bbox": bboxes,
                                "segmentation": [],
                                "area": None,
                                "iscrowd": None
                            })
                            data["categories"].append({
                                "id": category,
                                "name": process(category),
                                "supercategory": return_super(category)
                            })
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)


if __name__ == '__main__':
    # combine_to_dir()
    # make_coco()
    # serialize()
    check()
