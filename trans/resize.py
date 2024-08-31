import cv2
import numpy as np


"""
> opencv 缩放的 api

resize(src, dst, dsize, fx, fy, interpolation)

"""

def main():

    img = cv2.imread("./images/back.jpg", cv2.IMREAD_COLOR)

    # 1. 根据指定缩放后的大小来实现 dsize: (x, y)
    # dst = cv2.resize(img, (200, 300))

    # 2. 指定缩放因子
    # dst = cv2.resize(img, None, None, 0.6, 0.6)

    # 3.指定缩放的差值算法
    dst = cv2.resize(img, (1000, 1500), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("size", dst)

    while True:

        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
