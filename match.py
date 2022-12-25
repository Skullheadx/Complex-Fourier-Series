import cv2
import numpy as np

BACKGROUND = (255, 255, 255)


# Requires Black and White image. Ignores white background to isolate black.
def image_to_list(path):
    output = []
    image = cv2.imread(path)
    for i, j in np.ndenumerate(image):
        x, y, _ = i
        if tuple(image[x, y]) != BACKGROUND:
            output.append((y, x))
    return np.array(output)

# NEGATIVE values are expected. since every value not found in target and is therefore wrong.
# should use cache, though I am not sure how to implement
def match(target, arr):
    right = 0
    wrong = 0
    for i in arr:
        if i in target:
            right += 1
        else:
            wrong += 1
    return (right-wrong) / target.size
