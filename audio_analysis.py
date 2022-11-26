import librosa
import json

x, sr = librosa.load('只因你太美.mp3')
_, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')
print(beat_times)

total_time = len(x)/sr
fps = 30

offset_list = [0]*int(30*total_time)
print(total_time)

template = [2, 10, 15, 20, 20, 20, 15, 10, 2]  # 9帧施加抖音特效

for beat_time in beat_times:
    index = int(beat_time*30)
    print(index)
    offset_list[index-4:index+4] = template

with open("offset_list.json", "w") as f:
    json.dump(offset_list, f)




