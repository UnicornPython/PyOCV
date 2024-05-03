import cv2

import numpy as np

def bcallback(value):
    print(value)

def gcallback(value):
    print(value)

def rcallback(value):
    print(value)

def main():

    # 创建窗口
    cv2.namedWindow("trackbar", cv2.WINDOW_NORMAL)

    # 创建 trackerbar
    cv2.createTrackbar("B", "trackbar", 0, 255, bcallback)
    cv2.createTrackbar("G", "trackbar", 0, 255, gcallback)
    cv2.createTrackbar("R", "trackbar", 0, 255, rcallback)

    img = np.zeros((360, 640, 3), np.uint8)

    while True:

        r = cv2.getTrackbarPos("R", "trackbar")
        g = cv2.getTrackbarPos("G", "trackbar")
        b = cv2.getTrackbarPos("B", "trackbar")

        # 获取当前的 trackbar 构建新的数组
        img[:] = [b, g, r]

        cv2.imshow("trackbar", img)

        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break;

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
