import cv2
import numpy as np

def main():

    # 创建一个单通道黑白图片
    img1 = np.zeros((200, 200), np.uint8)
    img2 = np.zeros((200, 200), np.uint8) 

    # 在两张图像上的不同位置构建两块白色区域
    img1[20:120, 20:120] = 105
    img2[80:180, 80:180] = 105

    # 当相同位置出现相同的数据的时候才表现为白色
    new = cv2.bitwise_and(img1, img2)

    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow("new", new)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
