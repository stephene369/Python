from moviepy.editor import VideoFileClip, concatenate_videoclips

# Charger les vidéos
clip1 = VideoFileClip("video1.mp4")
clip2 = VideoFileClip("video2.mp4")

# Coller les vidéos ensemble
final_clip = concatenate_videoclips([clip1, clip2], method="compose")

# Enregistrer le résultat dans un fichier
final_clip.write_videofile("videos_collees.mp4")

# Libérer les ressources
clip1.close()
clip2.close()
 