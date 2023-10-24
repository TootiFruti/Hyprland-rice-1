import os
import random
import sys

USER=sys.argv[1]
# USER='onion'
mode=sys.argv[3]
# path_to_wall_directory=f"/home/{USER}/Pictures/.wallpaper/"
path_to_wall_directory=sys.argv[2]

with open(f'/home/{USER}/.config/hypr/wallpaper_changer/prev_wall.txt', 'r') as f:
    data=f.read()
    f.close()
data=eval(data)
if mode=='n':
    wallpaper=random.choices(os.listdir(path_to_wall_directory))[0]
elif mode == 'p':
    wallpaper=data[1]
else:
    print('not a vaild option')
data[1]=data[0]
data[0]=wallpaper
with open(f'/home/{USER}/.config/hypr/wallpaper_changer/prev_wall.txt', 'w') as f:
    f.write(str(data))
    f.close()
cmd=f"""
#!/bin/bash 
swww img {path_to_wall_directory}{wallpaper}  --transition-type any
"""

path_sr=f"/home/{USER}/.config/hypr/wallpaper_changer/change_wall.sh"
with open(path_sr, "w") as f:
    f.write(cmd)
    f.close()
