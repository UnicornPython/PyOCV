#!python 

import cv2.cv2 as cv2


def main():
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    img = cv2.imread("D:/PyCode/OCVModule/images/back.jpg")
    cv2.imshow("img", img)

    key = cv2.waitKey(0)
    # 由于键盘编码总是使用两个字节表示，所以我们获取到 int 类型的 key 取出后两个字节
    # 得到的就是我们键盘编码的正确值
    if (key & 0xFF == ord("q")):
        exit()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
