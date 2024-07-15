from moviepy.editor import VideoFileClip
from print_color import print
from pathlib import Path
import glob
from os.path import join 
import time
import numpy as np 
from pathlib import WindowsPath

# videos type
video_extention = ['mp4'  , 'webm', 'avi']
# videos path
path="D:\\music\\music\\videos\\"
# videos destinantion
destination = "D:\\music\\music\\audios\\"
# color list
color=['green','blue']

music = Path(destination).glob("*")
M = []
for m in music : 
    M.append(m.stem)
print(M)
# loop on video file and converting
for extention in video_extention :
    for video_name in ( glob.glob(path+f"*.{extention}") ):
        
        if Path(video_name).name.split(".")[0] in M : 
            print(f"{video_name} exist",color='red')
            continue
        try : 
            # getting video clip
            video = VideoFileClip(video_name)
            
            # getting audio from video
            audio = video.audio
            audio_name = Path(video_name).stem

            # write audiofile
            #audio.set_a

            audio.write_audiofile(f'{join(destination , audio_name)}'+'.mp3')
            print ("Convert",Path(video_name),"to an mp3\n" , format='bold'
                    ,tag='Successful', tag_color=color[0], color=color[1])
            
            time.sleep(1)
        except Exception as e : 
            print(e)

