import os
import sys
from PIL import Image

size = (600, 400)

root = os.getcwd()
folder = root + "/supplier-data/images"

for subdir, dirs, files in os.walk(folder):
    for file in files:
        outfile = folder + "/" + file.split(".")[0] + ".jpeg"
        print("processing image: " + file + " to: " + outfile)
        try:
            with Image.open(folder + '/' + file, mode = 'r') as im:
                im = im.convert("RGBA")
                im.convert('RGB').resize(size).save(outfile, 'JPEG')
        except IOError:
            print('cannot create thumbnail for', file)
