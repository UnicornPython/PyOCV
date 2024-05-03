
import cv2
import numpy as np

"""
多边形的绘制
"""

def main():

    # 背景
    img = np.zeros((480, 640, 3), np.uint8)
    
    # 多边形的顶点
    points = np.array([(10, 100), (400, 20), (200, 20), (10, 100)], np.int32)
    
    # 绘制图形
    cv2.polylines(img, [points], False, (0, 255, 255), 1, 4)

    # 这里线型将不能对其填充
    # 需要使用 fillPoly() API 操作
    cv2.fillPoly(img, [points], (255, 0, 0), 8)

    cv2.imshow("line", img)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
