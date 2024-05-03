import numpy as np
import cv2

def main():

    img = np.zeros((480, 640, 3), np.uint8)

    # 拆分通道(形成了新的数据)
    b, g, r = cv2.split(img)

    b[10:100, 10:100] = 255
    g[10:100, 10:100] = 255

    # 合并通道
    img2 = cv2.merge((b,   g, r));

    cv2.imshow("img", img) 
    cv2.imshow("b", b)
    cv2.imshow("g", g)
    cv2.imshow("img2", img2)

    while True:
        key = cv2.waitKey(0);
        if key & 0xff == ord("q"):
            break 

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
