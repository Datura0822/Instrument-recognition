import cv2
import os
from PIL import Image
import numpy as np
import random

def saltNoise(img, per):
    num = int(img.shape[0] * img.shape[1] * per)
    for k in range(num):
        i = random.randint(0, img.shape[0]-1)
        j = random.randint(0, img.shape[1]-1)
        tmp = random.randint(0, 1)
        if tmp == 0:
            if img.ndim == 2:
                img[i,j] = 255
            elif img.ndim == 3:
                img[i,j,0]= 255
                img[i,j,1]= 255
                img[i,j,2]= 255
        else:
            if img.ndim == 2:
                img[i,j] = 0
            elif img.ndim == 3:
                img[i,j,0]= 0
                img[i,j,1]= 0
                img[i,j,2]= 0
    return img

def GaussianNoise(img,means,sigma,per):
    num=int(img.shape[0] * img.shape[1] * per)
    for k in range(num):
        i = random.randint(0, img.shape[0]-1)
        j = random.randint(0, img.shape[1]-1)
        if img.ndim == 2:
            img[i, j] = img[i, j] + random.gauss(means, sigma)
            if  img[i, j]< 0:
                 img[i, j]=0
            elif img[i, j]>255:
                 img[i, j]=255
        elif img.ndim == 3:
            for h in range(3):
                img[i, j, h] = img[i, j, h] + random.gauss(means, sigma)
                if  img[i, j, h]< 0:
                    img[i, j, h] = 0
                elif img[i, j, h]>255:
                    img[i, j, h]=255
    return img

def spot(img, i, j):
    for p in range(20):
        for q in range(20):
            if img.ndim == 2:
                img[i + p, j + q] = 0
            elif img.ndim == 3:
                img[i + p, j + q, 0] = 0
                img[i + p, j + q, 1] = 0
                img[i + p, j + q, 2] = 0
    return img

# a=random.randint(0,1)
file = os.listdir('../data/test/image_in')
file.sort()
base_dir = '../data/test/image_in/'
new_dir = '../data/test/image_out/'

# for img in file:
#     image = cv2.imread(base_dir + img)
#     image = saltNoise(image, 0.05)
#     cv2.imwrite(new_dir + img, image)

# for img in file:
#     image = cv2.imread(base_dir + img)
#     image = GaussianNoise(image, 18, 1.0, 0.32)
#     cv2.imwrite(new_dir + img, image)

image = cv2.imread(base_dir + '06.jpg')
image = spot(image, 150, 270)
cv2.imwrite(new_dir + '36.jpg', image)
