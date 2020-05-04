import glob
import os
import uuid 
from os import system

names = []
dir_input = os.path.dirname(os.path.abspath(__file__)) + "\\input"
dir_output = os.path.dirname(os.path.abspath(__file__)) + "\\output"

videos = glob.glob("./*.MP4")

for video in videos:
    names.append(video[2:])

name = uuid.uuid1().int

print(dir_input)

#for video in names:
    #print(f'ffmpeg -i "C:\\Users\\raizo\\Desktop\\frames\{video}" -vf fps=1/240 output/{name}.png'))


#for video in names:
#    name = uuid.uuid1().int
#    print(system(f'ffmpeg -i "C:\\Users\\raizo\\Desktop\\frames\\{video}" -vf fps=1/240 output/{name}.png'