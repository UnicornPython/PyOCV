import cv2


def main():

    # 只有两张图片大小，属性一致的时候才能融合
    source1 = cv2.imread("./images/123.jpg", cv2.IMREAD_COLOR)
    source2 = cv2.imread("./images/back.jpg", cv2.IMREAD_ANYCOLOR)

    # 按照权重进行融合(alpha + beta) 可以是高于或者低于, 等于1 的
    target = cv2.addWeighted(source1, 0.3, source2, 0.9, -100);

    cv2.imshow("target", target)
    
    while True:
        key = cv2.waitKey(20)
        if key & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
