from setup import *
from to_points import image_to_points
from order_points import order
from inverse_fft import IFFT
from draw import draw
from series import Series


def main():
    print("Complex Fourier Transforms")

    print(f"Converting {FILENAME} to points")
    points = image_to_points(FILEPATH)
    print("Ordering points")
    points = order(points)
    print("Inverse FFT")
    waves = IFFT(points)
    print("Drawing")
    draw(Series(waves))


if __name__ == "__main__":
    main()
