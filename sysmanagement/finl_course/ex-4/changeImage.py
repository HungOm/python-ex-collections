#!/usr/bin/env python3
import os
from PIL import Image


path = os.getcwd()+'/supplier-data/images'
size =(600,400)

for root, dirs, files in os.walk(path, topdown=True):
    print(root)
    for name in files:
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpeg"):
                print("A jpeg file already exists for %s" % name)
            # If a jpeg is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpeg"
                try:
                    im = Image.open(os.path.join(root, name))
                    # remove alpha in rgba by converting it to rgb 
                    rgb_im = im.convert('RGB')
                    print("Generating jpeg for %s" %name )
                    rgb_im.thumbnail(size)
                    rgb_im.save(outfile, "JPEG", quality=100)
                    os.remove(os.path.join(root,name))
                    print("Removed all tiff")
                except Exception as e:
                    print(e)