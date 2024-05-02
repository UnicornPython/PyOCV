import cv2

"""
open 源码中关于视频处理的 API 定义位于 
 
- 文件存在 `opencv/modules/videoio/include/opencv2/videoio.hpp`

"""

def main():

    cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)

    # 开启摄像头抓取视频帧
    cap = cv2.VideoCapture(0)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 设置视频帧的编码格式
    fourcc = cv2.VideoWriter.fourcc("X","V","I","D")

    # 构建视频文件写入对象
    vw = cv2.VideoWriter("./videos/record.avi", fourcc, 30, (width, height))
                                                            
    # 如果摄像头是打开成功了, 则处理数据
    while cap.isOpened():
        status, frame  = cap.read()

        if not status:
            print("采集视频帧出错")
            break;

        # 在窗口上先显示出图像
        cv2.imshow("video", frame)

        # 采集的视频写入到文件中
        vw.write(frame)

        key = cv2.waitKey(30)
        if key & 0xff == ord('q'):
            break;

    # 释放资源
    cap.release()
    vw.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
