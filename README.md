# Beat Track Douyin
基于背景音频节拍点实现视频抖音特效

## 环境
- python
- ffmpeg

## 运行步骤
### 提取音频
```sh
ffmpeg -i 只因你太美.mp4 只因你太美.mp3
```

### 音频分析
```shell
python audio_analysis.py
```

### 视频处理
```shell
python video_process.py
```

### 合并音频和处理后的视频
```shell
ffmpeg -i output.avi -i 只因你太美.mp3 -c copy output.mp4
```

### 查看效果
见：output.mp4


## 参考
- https://librosa.org/doc/main/generated/librosa.beat.beat_track.html
- https://blog.csdn.net/python2021_/article/details/120002570