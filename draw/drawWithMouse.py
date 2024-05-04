import numpy as np
import cv2

# 定于当前的绘制的模式
mode = "line"
# 默认的绘制的起点
startPos = (0, 0)

# 设置初始背景图像
img = np.zeros((480,  640, 3), np.uint8)

def mcallback(event, x, y, flag, usedata):

    global startPos, mode

    if (event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startPos = (x, y)
    elif (event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if mode == "line":
            cv2.line(img, startPos, (x,y), (0, 255, 255))  
        if mode == "rectangle":
            cv2.rectangle(img, startPos, (x, y), (0, 255, 255))
        if mode == "circle":
            a = (x - startPos[0])
            b = (y - startPos[1])
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv2.circle(img, startPos, r, (0, 255, 255))
        if not mode:
            print("请线选择绘制的图形")

def main():

    global mode, img

    cv2.namedWindow("drawShape", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("drawShape", mcallback)

    while True:

        cv2.imshow("drawShape", img)
        key = cv2.waitKey(20)
        if key & 0xff == ord("c"):
            mode = "circle"
        elif key & 0xff == ord("r"):
            mode = "rectangle"
        elif key & 0xff == ord("l"):
            mode = "line"
        elif key & 0xff == ord("w"):
            img = np.zeros((480, 640, 3), np.uint8)
        elif key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
