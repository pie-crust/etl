import sys
from pprint import pprint
from moviepy.editor import VideoFileClip, vfx
e=sys.exit

video = VideoFileClip(r'C:\Users\alex_\OneDrive\Desktop\Matsuev_Video_Flat_Curve\C0006.MP4')
out = video.rotate(90)
pprint(dir(vfx))
#e()
out.write_videofile(r'C:\Users\alex_\OneDrive\Desktop\Matsuev_Video_Flat_Curve\C0006_rotated.MP4')