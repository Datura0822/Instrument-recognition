import cv2
import os
import numpy as np
from hough import hough
from operators import read_write

def min_fun(param):

    file = os.listdir('../data/train/image_out')
    file.sort()
    base_dir = '../data/train/'
    data = read_write.my_open(base_dir + 'input.txt')

    minf = []
    # cnt = 0
    for img in file:
        src = np.load(base_dir + 'image_out/' + img)
        src = src[:, :280]
        current_value = hough.hough(src, param[0], param[1], param[2]) * 10 / 27 + param[3]
        cnt = int(img[0])
        minf.append(abs(data[cnt] - current_value))
        # print (cnt, data[cnt])
        # cnt = cnt + 1

    return minf
