import cv2
import pyautogui
import numpy as np
from datetime import datetime

# 设置捕获电脑区域
monitor = (0, 0, 1920, 1080)

# 视频保存参数
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 25.0
output_size = (1920, 1080)
output_file = "videos/screen_capture.avi"

# 创建 VideoWriter 对象
out = cv2.VideoWriter(output_file, fourcc, fps, output_size)

# 创建 windows 窗体
cv2.namedWindow(
    "实时屏幕捕获".encode("gbk").decode("UTF-8", errors="ignore"), cv2.WINDOW_NORMAL
)

while True:

    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 设置捕获对象
    screenshot = pyautogui.screenshot(region=monitor)
    screenshot_np = np.array(screenshot)

    # 将 BGR 转换为 RGB (OpenCV 默认使用 RGB)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

    # 在窗口内显示实时时间
    cv2.putText(
        screenshot_np,
        current_time,
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2,
        cv2.LINE_AA,
    )

    # 将帧写入视频流
    out.write(screenshot_np)

    # 显示屏幕截取画面
    cv2.imshow(
        "实时屏幕捕获".encode("gbk").decode("UTF-8", errors="ignore"), screenshot_np
    )

    # 监控按键，按下 q 退出程序
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 关闭 OpenCV 所有窗体
cv2.destroyAllWindows()
