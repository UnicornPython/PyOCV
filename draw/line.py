import cv2

import numpy as np


def main():

    # 背景
    img = np.zeros((480, 640, 3), np.uint8)

    # 画线, 座标点
    cv2.line(img, (10, 20),(300, 400), (0, 0, 255), 5, 16)
    cv2.line(img, (90, 100),(380, 480), (0, 255, 255), 5, 4)

    cv2.imshow("line", img)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
