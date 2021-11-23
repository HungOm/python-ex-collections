#! /usr/bin/env python3
import os
import requests

DIR = 'supplier-data/descriptions'


def serialize_file_content(dir):
        abs_path = os.path.abspath(dir)
        ls = []
        fields=['name','weight','description','image_name']
        for root,directory,files in os.walk(abs_path,topdown=True):
            for file in files:
                obj = {}

                with open(os.path.join(root,file)) as f:
                    count = 0
                    for line in f:
                        obj[fields[count]]=line.strip()
                        # if fields[] == 'image_name':
                        name = file.split('.')[0]
                        obj[fields[3]]=name +'.jpeg'
                      

                        count += 1
                ls.append(obj)
            
        return ls


if __name__ =='__main__':   
    objects = serialize_file_content(DIR) 
    for obj in objects:
        obj["weight"] = int(obj["weight"].split(' ')[0])

        # print(obj)
        status = requests.post('http://34.67.161.173/fruits/',data=obj)
        print(status)
    # print(make_json(DIR))