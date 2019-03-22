
# Pyton program to Convert a video file to audio


import moviepy.editor as mp
video = mp.VideoFileClip("test.mp4")
video.audio.write_audiofile("test.mp3")



# ================ OUTPUT ================

# MoviePy - Writing audio in %s
# MoviePy - Done.


