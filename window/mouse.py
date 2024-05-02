import cv2

import numpy as np

"""
鼠标控制 c++ 中源代码中的定义

- `opencv/modules/highgui/include/opencv2/highgui.hpp

"""

def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


def main():

    cv2.namedWindow("mouse", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("mouse", 640, 360)

    # 设置鼠标回调
    cv2.setMouseCallback("mouse", mouse_callback, "123")


    # 构建一个数据用于显示
    # 这里是 BGR 数组，因此和图片的宽高需要反过来
    img = np.zeros((360, 640, 3), np.uint8)

    while True:

        cv2.imshow("mouse", img)

        key = cv2.waitKey(0)

        if key & 0xff == ord("q"):
            break;
        
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
