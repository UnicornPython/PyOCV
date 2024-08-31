import cv2
import numpy as np


def main():

    img = cv2.imread("./images/back.jpg", cv2.IMREAD_COLOR)
    (h, w, c) = img.shape

    # 变换矩阵怎么出来的
    # 对于平移来说,需要一个 2 * 3 的矩阵，
    # 是一个单元矩阵[[1,0],[0, 1]] 添加偏移量-> [[1,0,100], [0, 1, 200]] 
    # 这里分别对应的是 x, y 轴的偏移量
    M = np.float32([[1, 0, 100], [0, 1, 200]]) # 有精度要求，需要 float32,
    new = cv2.warpAffine(img, M, dsize=(w, h)) 

    cv2.imshow("img", img) 
    cv2.imshow("new", new)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()    


