import cv2
import numpy as np

"""
1. 引入一幅图片
2. 自己制作一个logo
3. 在 logo 位置做一个处理
4. 使用 add() 将图片与 log 融合
"""


def main():

    img = cv2.imread("./images/back.jpg")

    logo = np.zeros((200, 200, 3), np.uint8)

    mask = np.zeros((200, 200), np.uint8)

    # 制作logo
    logo[10:120, 20:120] = [0, 0, 255]
    logo[80:180, 80:180] = [0, 255, 0]

    mask[20:120, 20:120] = 255
    mask[80:180, 80:180] = 255

    cv2.imshow("mask", mask)
    cv2.imshow("logo", logo)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
