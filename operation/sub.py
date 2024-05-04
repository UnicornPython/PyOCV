import cv2 
import numpy as np


def main():

    # 读取原始图片
    img = cv2.imread("./images/dog.jpg", cv2.IMREAD_COLOR)

    # 构建减量的矩阵
    sub = np.ones((img.shape), np.uint8) * 20

    value = cv2.subtract(img, sub)

    cv2.imshow("before", img)
    cv2.imshow("after", value)

    while True:
        key = cv2.waitKey(20)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
