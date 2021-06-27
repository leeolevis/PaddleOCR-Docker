#coding:utf-8
'''
@version: python3.6
@author: ‘eric‘
@license: Apache Licence
@contact: steinven@qq.com
@software: PyCharm
@file: client_test.py
@time: 2021/6/27 17:01
'''
import base64
import json
import os

import requests


def cv2_to_base64(image):
    return base64.b64encode(image).decode('utf8')

url = "http://172.16.71.234:9998/ocr/prediction"
test_img_dir = '../test_files'
for idx, img_file in enumerate(os.listdir(test_img_dir)):
    with open(os.path.join(test_img_dir, img_file), 'rb') as file:
        image_data1 = file.read()
    image = cv2_to_base64(image_data1)
    data = {"key": ["image"], "value": [image]}
    r = requests.post(url=url, data=json.dumps(data))
    print(r.json())

print("==> total number of test imgs: ", len(os.listdir(test_img_dir)))