#! /usr/bin/env python3

# import required libraries
import os
import requests
import json

# instantiate variables
fdict = {}

# set variable to storage location of description files
# desc_path = "/supplier-data/descriptions"
desc_path = "C:/Users/gscot/Documents/python/google-it-cert-final-project/supplier-data/descriptions"
# img_path = "/supplier-data/images"
img_path = "C:/Users/gscot/Documents/python/google-it-cert-final-project/supplier-data/images"

os.chdir(desc_path)
# get list and number of files
file_list = os.listdir()
num_files = len(file_list)

for file in file_list:
    with open(file, "r") as f:
        name_no_ext = file.split(".")[0]
        img_name = name_no_ext + ".jpeg"
        fname = f.readline()
        fweight = f.readline()
        fdesc = f.readline()
        fdict = dict({"name": fname.rstrip(),
                      "weight": int(fweight.split()[0].rstrip()),
                      "description": fdesc.rstrip(),
                      "image_name": img_name})
        f.close()
    fruit = json.dumps(fdict)
    print("uploading : ", fname)
    post = requests.post("http://[linux-instance-external-IP]/fruits/", json=fruit)

