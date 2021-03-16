import cv2
import numpy as np
# from PIL import Image

# 读入图像
src = cv2.imread('../data/train/1/1.jpg')
# cv2.imshow("hough lines", src)


# (width, height, x) = src.shape
# mid = int(height/2)
# src_left = src[0:width, 0:mid]
# src_right = src[0:width, mid:height]


def hough(img):
    # 中值滤波
    # median = cv2.medianBlur(img, 5)
    median = cv2.GaussianBlur(img, (3, 3), 0)
    # 灰度图
    gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
    # 边缘检测
    edges = cv2.Canny(gray, 50, 100)

    dst1 = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    aa = [181, 28, 159]  # 0.45, 0.1, 0.7
    minLineLength = int(aa[0])
    maxLineGap = int(aa[1])
    threshod = int(aa[2])
    lines1 = cv2.HoughLines(edges, 1, np.pi / 180.0, threshod, minLineLength, maxLineGap)
    s = 0
    if lines1 is not None:
        _lines1 = lines1[:, 0, :]  # 提取为二维
        i = 0.0
        s_rho = 0.0
        s_theta = 0.0
        for rho, theta in _lines1[:]:
            print(theta)
            i = i + 1
            s_rho = s_rho + rho
            s_theta = s_theta + theta
            a = np.cos(theta)
            b = np.sin(theta)
            x0, y0 = a * rho, b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * a))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))
            # cv2.line(dst1, pt1, pt2, (0, 255, 0), 2)
        s_theta = s_theta / i
        s_rho = s_rho / i
        a = np.cos(s_theta)
        b = np.sin(s_theta)
        x0, y0 = a * s_rho, b * s_rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * a))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))
        # cv2.line(dst1, pt1, pt2, (0, 0, 255), 2)
        s = s_theta
    # cv2.imshow("hough lines", dst1)
    # cv2.waitKey(0)
    return s


theta = hough(src)
print(theta)
