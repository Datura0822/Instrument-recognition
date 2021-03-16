import os
import cv2
from PIL import Image
import numpy as np
from operators import read_write

file = os.listdir('../data/train/image_in')
base_dir = '../data/train/image_in/'
new_dir = '../data/train/image_out/'

# file = os.listdir('../data/test/image_in')
# file.sort()
# base_dir = '../data/test/image_in/'
# new_dir = '../data/test/image_out/'

# file = os.listdir('../data/img')
# base_dir = '../data/img/'
# new_dir = '../data/img/'

size_m = 500
size_n = 500

for img in file:
    # image = Image.open(base_dir + img)
    # image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
    # image_size.save(base_dir + img)

    src = cv2.imread(base_dir + img) # 读取图像
    gauss = cv2.GaussianBlur(src, (15, 15), 0) # 高斯滤波
    gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY) # 转换为灰度图像
    # gray[gray < 100] = 0
    # gray[gray >= 100] = 255
    # gray = cv2.GaussianBlur(gray, (9, 9), 0)
    # gray[gray < 30] = 0
    # gray[gray >= 30] = 255

    edges = cv2.Canny(gray, 50, 100) # 边缘检测
    # cv2.imshow('gauss',gauss)
    np.save(new_dir + img, edges) # 存储处理好的图像

# src = cv2.imread(base_dir + file[0])
# gauss = cv2.GaussianBlur(src, (9, 9), 0)
# gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
# gray[gray<60] = 0
# gray[gray>=60] = 255
# gray = cv2.GaussianBlur(gray, (9, 9), 0)
# gray[gray<30] = 0
# gray[gray>=30] = 255
# cv2.imwrite('../data/train/gray.jpg', gray)
# cv2.imshow('gauss',gauss)
# cv2.waitKey(0)
