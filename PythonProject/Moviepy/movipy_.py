from moviepy.editor import *
import numpy as np 

clips = [ImageClip("image1.png").set_duration(5),
         ImageClip("image2.png").set_duration(5),
         ImageClip("image3.png").set_duration(5)]

transitions = ['slide_in_from_left', 'slide_in_from_right']
final_clip = concatenate_videoclips([CompositeVideoClip([c.fx(transitions[i]) for i, c in enumerate(clips)])])

# Écrire la vidéo dans un fichier
final_clip.write_videofile("ma_video.mp4")







#### other way


clip = ImageSequenceClip(["image3.png","image2.png","image3.png"], fps = 3)
  
# showing  clip 
clip.ipython_display(width = 360) 
