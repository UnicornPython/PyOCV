import cv2 

"""
> 图像的旋转

"""

def main():

    img = cv2.imread("./images/back.jpg", cv2.IMREAD_COLOR)

    img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img180 = cv2.rotate(img, cv2.ROTATE_180)
    img270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow("source", img)
    cv2.imshow("90", img90)
    cv2.imshow("180", img180)
    cv2.imshow("270", img270)

    while True:
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

if __name__ == "__main__":
    main()
