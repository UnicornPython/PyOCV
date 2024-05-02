import cv2


def main():

    #  构建窗口
    cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)
    # 获取视频设备

    # 1. 从本地设备的默认相机获取视频帧
    # cap = cv2.VideoCapture(0)

    # 2. 从文件获取视频帧数
    cap = cv2.VideoCapture("/home/unicorn/Pictures/idea.mkv")

    while True:
        status, img = cap.read()
        if not status:
            print("获取视频帧错误")
            exit()
        cv2.imshow("video", img)

        key = cv2.waitKey(20)
        if key & 0xff ==  ord("q"):
            break;

    # 释放 VideoCapture 资源
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
