from moviepy.editor import VideoFileClip

vid = VideoFileClip(r"""/home/kaneki/Videos/anime/Weathering With You [1080p][Dual].mkv""")

v = vid.subclip(90*60+10 , 100*60 )
v.write_videofile("/home/kaneki/Desktop/weathering1.mp4")


## 



