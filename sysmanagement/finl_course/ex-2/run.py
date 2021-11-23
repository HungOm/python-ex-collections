#! /usr/bin/env python3
import os
import requests


files = os.listdir('/data/feedback')
abs_path = os.path.abspath('/data/feedback')

def filetojson(file):
        fields=['title','name','date','feedback']
        obj = {}
        with open(os.path.join(abs_path,file)) as f:
                count = 0
                for line in f:
                        obj[fields[count]] = line.strip()
                        count += 1
        return obj


for file in files:
        jsonObj= filetojson(file)
        requests.post('http://34.134.74.6/feedback/',data=jsonObj)

