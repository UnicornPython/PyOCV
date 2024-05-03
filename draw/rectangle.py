import cv2
import numpy as np


def main():

    # 背景
    img = np.zeros((480, 640, 3), np.uint8)

    # 矩形
    # 传入的是对角线顶点，确定矩形
    cv2.rectangle(img, (10, 10), (100, 300), (0, 0, 255), -1)

    cv2.imshow("line", img)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
