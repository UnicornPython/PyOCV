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

    # 设置 logo 的大小
    logo = np.zeros((200, 200, 3), np.uint8)
    mask = np.zeros((200, 200), np.uint8)

    # 制作logo
    logo[20:120, 20:120] = [0, 0, 255]
    logo[80:180, 80:180] = [0, 255, 0]

    mask[20:120, 20:120] = 255
    mask[80:180, 80:180] = 255

    # 按位求反(logo所在的区域为黑色，其余部分为白色)
    m = cv2.bitwise_not(mask)

    # 选择位置
    roi = img[0:200, 0:200] 

    # 与图像内容进行融合
    tmp = cv2.bitwise_and(roi, roi, mask=m)

    # 与logo 部分进行叠加
    dst = cv2.add(tmp, logo)

    img[0:200, 0:200] = dst


    cv2.imshow("mask", mask)
    cv2.imshow("logo", logo)
    cv2.imshow("tmp", tmp)
    cv2.imshow("m", m)
    cv2.imshow("dst", dst)
    cv2.imshow("img", img)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
