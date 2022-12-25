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
