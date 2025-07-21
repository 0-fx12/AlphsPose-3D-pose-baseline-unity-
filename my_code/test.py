import os

import cv2


def split_video_into_frames(video_path, output_folder):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    # 检查视频文件是否成功打开
    if not video.isOpened():
        print("无法打开视频文件")
        return

    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 逐帧读取视频并保存为JPG图像文件
    frame_count = 0
    while True:
        # 读取一帧图像
        ret, frame = video.read()

        # 检查是否成功读取图像帧
        if not ret:
            break

        # 生成输出图像文件路径
        output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")

        # 保存图像帧为JPG文件
        cv2.imwrite(output_path, frame)

        frame_count += 1

    # 释放视频对象
    video.release()

    print(f"视频已分解为 {frame_count} 帧图像文件")


# 示例用法
video_path = "C:\\Users\\23114\\Desktop\\4月22日.mp4"  # 输入视频文件路径
output_folder = "output_frames"  # 输出图像帧文件夹路径

split_video_into_frames(video_path, output_folder)