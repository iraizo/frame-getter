import glob
import os
import uuid 
from os import system
from pathlib import Path
import time

output = []
dir_input = os.path.dirname(os.path.abspath(__file__)) + "\\input\\"
dir_output = os.path.dirname(os.path.abspath(__file__)) + "\\output\\"
directory = os.getcwd()
videos = glob.glob("./input/*.MP4")

# rename all files random
files = os.listdir(directory + "\\input")

for index, file in enumerate(files):
    name = uuid.uuid1().int
    os.rename(os.path.join(directory + "\\input", file), os.path.join(directory + "\\input", ''.join([str(uuid.uuid1().int), '.mp4'])))
    



files = os.listdir(directory + "\\input") # update files if needed, probaly not


# actually run ffmpeg
for video in files:
  name = uuid.uuid1().int
  print(system(f'ffmpeg -i "C:\\Users\\raizo\\Desktop\\frames\\input\\{video}" -vf "select=\'if(not(floor(mod(t,5)))*lt(ld(1),1),st(1,1)+st(2,n)+st(3,t));if(eq(ld(1),1)*lt(n,ld(2)+8),1,if(trunc(t-ld(3)),st(1,0)))\'" -vsync 0 {dir_output}{name}_out%d.png'))

