import cv2
import numpy as np

def main():

    img = cv2.imread("./images/dog.jpg", cv2.IMREAD_COLOR)

    # 图的加法就是矩阵的加法
    # 因此加法运算的两张图必须是相等大小的

    value = np.ones((img.shape), np.uint8) * 10
    # 对图像进行相加
    result = cv2.add(img, value)
    # 原图
    cv2.imshow("before", img)
    # 处理之后的图片
    cv2.imshow("after", result)

    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()




