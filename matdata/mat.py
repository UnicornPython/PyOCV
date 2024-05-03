import cv2

def main():

    img = cv2.imread("./images/back.jpg")
    # 浅拷贝
    img2 = img
    # 使用 copy 完成深拷贝
    img3 = img.copy()

    # 修改 img 图片的数据，看那些会变
    # 会变的就是浅拷贝, 共享了底层数据
    img[10:100, 10:100] = [0, 0, 255]

    cv2.imshow("img", img)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows();

if __name__ == "__main__":
    main()
