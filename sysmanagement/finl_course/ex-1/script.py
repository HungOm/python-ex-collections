#!/usr/bin/env python3
import os
from PIL import Image


path = os.getcwd()+'/images'
size =(128,128)


def get_nesteddirectory():
    dir = os.path.join(os.getcwd(), '/opt/icons/')
   # print(os.getcwd())
    if not os.path.isdir(dir):
        os.makedirs(dir)
    return dir

for root, dirs, files in os.walk(path):
    for file in files:
        newPath = get_nesteddirectory()
        try:
            with Image.open(os.path.join(root,file)) as im:
                if im.mode != "RGB":
                    im1 = im.resize(size=size)
                    im2 = im1.convert("RGB")
                    im2.transpose(Image.ROTATE_90)
                    im2.save("{}{}".format(newPath,file), "JPEG")
                    print('size: {},mode: {},format: {}'.format(im2.size,im2.mode,im2.format))
                    print("{}.jpeg is successfully created at {}".format(file,newPath))
        except OSError as e:
            print("Cannot convert image for",e)