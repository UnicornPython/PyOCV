import cv2


def main():

    img = cv2.imread("./images/back.jpg")

    # 获取属性
    print(img.shape)   # 获取 高度, 长度，通道数
    print(img.size)    # 大小 : 高度 * 长度 * 通道数
    print(img.dtype)  # 图像的位深


if __name__ == "__main__":
    main()
