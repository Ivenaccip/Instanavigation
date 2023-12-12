#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo "Corre como root"
    exit 1
fi

USER_NAME="kroonadmin"

sudo -u $USER_NAME python3 google_sele.py

user="kroonadmin"

origin="/home/${user}/Downloads"
destination=$(pwd)
directory="./"

find ${origin} -type f -name "*.html" -exec mv {} ${destination} \;

for file in ${directory}*html; do
	if [ -f "$file" ]; then
		mv "$file" "${file%.html}.txt"
	fi
done