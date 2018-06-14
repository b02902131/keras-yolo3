# Title:
# Author:   Bigyo
# Date:     2018.6.12
# Details:
#   Convert the label data from the format of
#       [unsky's](https://github.com/unsky/yolo-for-windows-v2#how-to-train-to-detect-your-custom-objects)
#       >>> which is <object-class> <x> <y> <width> <height>
#       >>> seperate with space
#       to
#       [qqwweee's]
#       >>> which is x_min,y_min,x_max,y_max,class_id
#       >>> seperate with comma
#       >>> rects seperate with space

import os
from os import listdir
from os.path import isfile, join

from PIL import Image

out_file = open("Fish/train.txt", "w")

base_folder = os.path.dirname(os.path.abspath('__file__'))

fish_folder = os.path.join(base_folder, "Fish/original")

p = fish_folder
file_list = [f for f in listdir(p) if isfile(join(p, f))]
index_list=  [f.split('.')[0] for f in file_list if f.split('.')[-1] == 'txt']

for index in index_list:
    label_file = index + ".txt"
    img_file = index + ".jpg"
    out_file.write(os.path.join(fish_folder, img_file))
    im = Image.open(os.path.join(fish_folder, img_file))
    img_w, img_h = im.size
    rect_file = open(os.path.join(fish_folder, label_file))
    for rect in rect_file:
        out_file.write(" ")
        objClass, x, y, width, height = rect.split(" ")
        x_min = int(float(x) * img_w)
        y_min = int(float(y) * img_h)
        x_max = int((float(x) + float(width)) * img_w)
        y_max = int((float(y) + float(height)) * img_h)
        out_file.write(str(x_min)+","+str(y_min)+","+str(x_max)+","+str(y_max))
        out_file.write(","+objClass)
    out_file.write("\n")
