import json
import cv2

def check():
    images_path = '/home/casper/Desktop/Vidrone/images/uav0000013_00000_v0000003.jpg'
    with open('/home/casper/Desktop/Vidrone/data_file.json') as f:
        data = json.load(f)
    image = cv2.imread(images_path)
    for i in data['annotations'] :
        if i == {}:
            continue
        else:
            if i['image_id'] == '1':
                if  i['bbox'] :
                    window_name = 'Image'
                    x = i['bbox']
                    start_point = (int(x[0]), int(x[1]))
                    end_point = (int(x[2]), int(x[3]))
                    thickness = 2
                    color = (255, 0, 0)
                    image = cv2.rectangle(image, start_point, end_point, color, thickness)
                    cv2.imshow(window_name, image)
                    cv2.waitKey()




