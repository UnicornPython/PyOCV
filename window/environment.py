#!python 

import cv2


"""
opencv 中关于 windows 操作的定义在
`opencv/modules/highgui/include/opencv2/highgui.hpp`

"""


def main():
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    img = cv2.imread("./images/back.jpg")
    cv2.imshow("img", img)

    key = cv2.waitKey(0)
    # 由于键盘编码总是使用两个字节表示，所以我们获取到 int 类型的 key 取出后两个字节
    # 得到的就是我们键盘编码的正确值
    if (key & 0xFF == ord("q")):
        exit()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
