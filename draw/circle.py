

import cv2

import numpy as np


def main():

    # 背景
    img = np.zeros((480, 640, 3), np.uint8)

    # 圆形
    cv2.circle(img, (300, 300), 100, (0, 0, 255))
    # 线型为 -1 时填充为一个实心的圆形
    cv2.circle(img, (300, 300), 5, (0, 0, 255), -1)

    cv2.imshow("line", img)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
