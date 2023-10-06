#!python

import cv2.cv2 as cv2

"""
> opencv 中加载图片
"""


def main():
    cv2.namedWindow("img")
    img = cv2.imread("../images/back.jpg")
    cv2.imshow('img', img)

    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        exit(0)
    else:
        print("other")


if __name__ == "__main__":
    main()
