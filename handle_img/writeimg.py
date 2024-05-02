import cv2

def main():

    cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
    img = cv2.imread("./images/123.jpg")
    cv2.imshow("img", img)

    while True:
        key = cv2.waitKey(0)
        if (key & 0xff == ord("q")):
            break
        elif key & 0xff == ord("s"):
            cv2.imwrite("./images/123.jpg", img)
            break

    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
