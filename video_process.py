import json
import os
import cv2
import numpy as np
import copy
from PIL import Image


imagepath = "1.png"


def image_douyin(img, offset):
    img_arr = np.array(img)
    # 提取R
    img_arr_r = copy.deepcopy(img_arr)
    img_arr_r[:, :, 0:2] = 0
    # 提取GB
    img_arr_gb = copy.deepcopy(img_arr)
    img_arr_gb[:, :, 2] = 0
    # 创建画布把图片错开放
    canvas = copy.deepcopy(img_arr)
    canvas[offset:, offset:, ] = 0   # 小于offset的不变，防止黑边
    canvas[offset:, offset:, 2] = img_arr_r[offset:, offset:, 2]  # 放置R图层
    canvas[offset:, offset:, 0:2] = img_arr_gb[:img_arr_gb.shape[0]-offset, :img_arr_gb.shape[1]-offset, 0:2]  # 错位GB图层

    return canvas



video_path = "只因你太美.mp4"
with open("offset_list.json", "r") as f:
    offset_list = json.load(f)

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    print("打开视频失败！")

fps = capture.get(cv2.CAP_PROP_FPS)
size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fNUMS = capture.get(cv2.CAP_PROP_FRAME_COUNT)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, size)

print("fps:", fps)
print("size:", size)
print("fNUMS:", fNUMS)

# cv2.namedWindow("test", 0)
# cv2.moveWindow("test", 100, 100)
# cv2.resizeWindow("test", 960, 640)
f_cnt = 0
while True:
    _, frame = capture.read()
    if frame is None:
        break

    offset = offset_list[f_cnt]
    if offset == 0:
        frame_douyin = frame
    else:
        frame_douyin = image_douyin(frame, offset)
    f_cnt += 1
    print(f"processing {f_cnt}/{fNUMS} ....")
    # img proc ...
    # cv2.waitKey(30)
    # cv2.imshow("test", frame_douyin)
    out.write(frame_douyin)

out.release()
capture.release()