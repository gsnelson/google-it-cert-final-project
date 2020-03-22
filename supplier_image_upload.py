#!/usr/bin/env python3
import requests

root = os.getcwd()
folder = root + "/supplier-data/images"
url = "http://[linux-instance-IP-Address]/media/images/"

for subdir, dirs, files in os.walk(folder):
    for file in files:
        if names.endswith(".jpeg"):
            with open(file, "rb") as opened:
                r = requests.post(url, files={"file": opened})
