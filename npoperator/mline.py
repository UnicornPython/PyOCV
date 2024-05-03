import numpy as np
import cv2

def main():

    # 构建一个黑色的背景
    img = np.zeros((360, 640, 3), np.uint8)

    # 这里对应的是这个行列号下的一组数据
    print(img[100, 100])

    # 将背景中的某个方向上修改，将变成一条直线
    count = 0
    while count < 200:
        # 3 个 通道都赋值 255 (白色)
        # img[count, 100] = 255

        # 按照BRG(012), 对单一通道(2)赋值 (红色)
        # img[count, 100, 2] = 255

        # 使用数组指定每一个通道的值
        img[count, 100] = [0, 255, 0]

        count = count + 1

    cv2.imshow("line", img)
    while True:
        key = cv2.waitKey(0)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
