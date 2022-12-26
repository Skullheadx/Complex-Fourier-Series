import cv2
import numpy as np

BACKGROUND = (255, 255, 255)


# Requires Black and White image. Ignores white background to isolate black.
def image_to_list(path):
    output = []
    image = cv2.imread(path)
    width, height, _ = image.shape
    for i, j in np.ndenumerate(image):
        x, y, _ = i
        if tuple(image[x, y]) != BACKGROUND:
            output.append((y -height/2, x-width/2))
    return np.array(output)


def match(target, arr):
    right = 0
    for i in arr:
        x1,y1 = i
        for j in target:
            x2,y2 = j
            if pow(x2-x1,2) + pow(y2-y1,2) < 225: # 15 ^2
                right += 1

    # print(right/arr.size, arr)
    return (right) / arr.size
