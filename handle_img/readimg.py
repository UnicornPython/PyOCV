#!python

import cv2 

"""
> opencv 中加载图片
-------------------------------------------------------
C++ 源码中定义的位置 
    `opencv/modules/imgcodecs/include/opencv2/imgcodecs.hpp`

"""


def main():
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    # 图片加载，默认是(IMREAD_COLOR)彩色模式
    # 可以使用其他色彩模式加载图片
    img = cv2.imread("./images/back.jpg", cv2.IMREAD_COLOR)
    cv2.imshow('img', img)
    while True:
        key = cv2.waitKey(0)
        if key & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            exit(0)
        else:
            print("other")


if __name__ == "__main__":
    main()
