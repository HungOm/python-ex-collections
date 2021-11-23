#!/usr/bin/env python3
import requests
import run

# This example shows how a file can be uploaded using
# The Python Requests module

# url = "http://localhost/upload/"
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})
DIR = 'supplier-data/descriptions'
print(run.serialize(DIR)[0]["name"])