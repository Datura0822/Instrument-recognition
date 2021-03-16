import cv2
import numpy as np

def hough(edges, minLineLength, maxLineGap, threshod):
    lines1 = cv2.HoughLines(edges, 1, np.pi / 180.0, int(threshod), int(minLineLength), int(maxLineGap))
    s = 0
    # num = 0
    if lines1 is not None:
        _lines1 = lines1[:, 0, :]
        i = 0
        # j = 0
        s_theta = 0.0
        for rho, theta in _lines1[:]:
            i = i + 1
            # if abs(theta-target_value) < 0.05 :
            #     j = j + 1
            s_theta = s_theta + theta
        s_theta = s_theta / i
        s = np.rad2deg(s_theta)
        # num = j
        #print(s)
    return s
