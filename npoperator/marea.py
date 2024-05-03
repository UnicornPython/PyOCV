import cv2
import numpy as np


def main():
    
    img = np.zeros((360, 640, 3), np.uint8)

    # 原始区域中的所有点位都进行修改
    # img[:,:] = [0, 255, 0] 
    # 简写方式
    img[:] = [0, 255, 0]

    # 其他的变化截取方式
    img[:, 10] = [0, 0, 255] # 表示 x 不变化，y 取所有

    # 在原始点位上截取一块区域
    img[10:200, 10:200, 0] = 255

    cv2.imshow("area", img)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
