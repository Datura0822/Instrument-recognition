import cv2
from PIL import Image
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def gray_level(img):
    w = img.shape[0]
    h = img.shape[1]
    value = [0] * 300
    for i in range(w):
        for j in range(h):
            value[img[i, j]] = value[img[i, j]] + 1;
    value = np.array(value)
    value = value / (w * h)
    return value



src = cv2.imread('../data/test/image_in/49.jpg')
# print(src)
median = cv2.GaussianBlur(src,(15,15),0)
gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
value = gray_level(gray)
print(value)
#
x = np.arange(0, 300)
print(x)
#
num_bins = 299
#
fig, ax = plt.subplots()
#
# # the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)
#
# # add a 'best fit' line
y = value[x]
print(y)
#
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# print(value)
# # Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
# print(gray[0])