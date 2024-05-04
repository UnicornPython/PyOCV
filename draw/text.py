import cv2
import numpy as np

def main():

    img = np.zeros((480, 640, 3), np.uint8)
    # 绘制字体
    cv2.putText(img, "hello\n world", (100, 300), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 255))

    cv2.imshow("text", img)

    while True:
        key = cv2.waitKey(10) 
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
