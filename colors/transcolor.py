import cv2

"""
> opencv 中关于颜色空间的定义

opencv/modules/imgproc/include/opencv2/imgproc.hpp

"""


def callback(value):
    print(value)
    pass

def main():

    cv2.namedWindow("color", cv2.WINDOW_NORMAL)

    # 色彩空间定义
    colorspace = [
            cv2.COLOR_BGR2BGRA, 
            cv2.COLOR_BGR2BGRA, 
            cv2.COLOR_BGR2GRAY, 
            cv2.COLOR_BGR2HSV_FULL, 
            cv2.COLOR_BGR2YUV,
    ]

    cv2.createTrackbar("cursor", "color", 0, 4, callback)

    img = cv2.imread("./images/back.jpg")

    while True:
        index = cv2.getTrackbarPos("cursor", "color")

        cvt_img = cv2.cvtColor(img, colorspace[index])

        cv2.imshow("color", cvt_img)

        key = cv2.waitKey(10)

        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
