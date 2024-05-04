import cv2
import numpy as np

def main():

    # 创建一个单通道黑白图片
    img = np.zeros((200, 200), np.uint8)

    img[50:150, 50:150] = 255

    new = cv2.bitwise_not(img)

    cv2.imshow("img", img)
    cv2.imshow("new", new)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
