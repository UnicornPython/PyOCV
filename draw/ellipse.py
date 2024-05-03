import cv2

import numpy as np


def main():

    # 背景
    img = np.zeros((480, 640, 3), np.uint8)

    # 圆形
    cv2.circle(img, (300, 300), 100, (0, 0, 255))
    cv2.circle(img, (300, 300), 5, (0, 0, 255), -1)

    # 椭圆
    # 以顺时针转的方式计算角度
    cv2.ellipse(img, (300, 300), (100, 50), 30, 0, 360, (0, 255, 255))
    # 以右侧长轴的端点为起点计算起始点和终止点的角度(如果绘制弧形)
    cv2.ellipse(img, (300, 300), (100, 50), 60, 0, 360, (0, 255, 255))
    cv2.ellipse(img, (300, 300), (100, 50), 90, 0, 260, (0, 255, 255))
    cv2.ellipse(img, (300, 300), (100, 50), 120, 0, 250, (0, 255, 255))
    cv2.ellipse(img, (300, 300), (100, 50), 150, 0, 240, (0, 255, 255))
    cv2.ellipse(img, (300, 300), (100, 50), 180, 0, 230, (0, 255, 255))

    cv2.imshow("line", img)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
