from setup import *

BACKGROUND = (255, 255, 255)


# Requires Black and White image. Ignores white background to isolate black.
def image_to_points(path):
    output = []
    image = cv2.imread(path)
    width, height, _ = image.shape
    for i, j in np.ndenumerate(image):
        x, y, _ = i
        if tuple(image[x, y]) != BACKGROUND:
            output.append((y - height / 2, x - width / 2))
    return np.array(output)
