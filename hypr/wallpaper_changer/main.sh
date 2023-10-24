#!/bin/bash

PATH_TO_WALL_DIRECTORY="/home/onion/Pictures/.wallpaper/"

python3 ~/.config/hypr/wallpaper_changer/wall_changer.py $USER $PATH_TO_WALL_DIRECTORY $1 &&
	~/.config/hypr/wallpaper_changer/change_wall.sh
