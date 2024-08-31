import cv2 


def main():

    img = cv2.imread("./images/back.jpg", cv2.IMREAD_COLOR)

    flip0 = cv2.flip(img, 0)
    flip1 = cv2.flip(img, 10)
    flip2 = cv2.flip(img, -2)

    cv2.imshow("flip", img)
    cv2.imshow("flip0", flip0)
    cv2.imshow("flip1", flip1)
    cv2.imshow("flip2", flip2)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
