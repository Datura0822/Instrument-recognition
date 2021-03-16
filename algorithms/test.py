import os
import cv2
import Config
import numpy as np
from hough import hough
from operators import read_write

file = os.listdir('../data/test/image_out')
file.sort()
base_dir = '../data/test/'
param = read_write.my_open(base_dir + 'input.txt')
value = read_write.my_open(base_dir + 'output.txt')

# 测试函数
data = []
error = []
cnt = 0
for img in file:
    src = np.load(base_dir + 'image_out/' + img)
    src1 = src[:, :275]
    src2 = src[:, 225:]
    current_value1 = hough.hough(src1, param[0], param[1], param[2])
    current_value2 = hough.hough(src2, param[0], param[1], param[2])

    ans = 0
    if current_value1 != 0:
        ans = current_value1
    elif current_value2 != 0:
        ans = current_value2 + 180

    if ans != 0:
        ans = ans * 10 / 27 + param[3]
        error.append(abs(value[cnt] - ans) / 100)
        data.append(round(ans, 1))
    else:
        data.append(00.0)
        error.append(abs(value[cnt]) / 100)

    cnt = cnt + 1

for i in range(50):
    print('%2s' % i, '%7.1f' % value[i], '%7.1f' % data[i], '%7.3f' % error[i])
