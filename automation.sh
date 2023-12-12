#!/bin/bash

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

for file in ${directory}*.txt; do
	echo "$file"
	if [[ "$file" == "${directory}requirements.txt" ]]; then
		continue
	else
		echo "Reading $file"
		cleaned_file="${file%.txt}_clean.txt"
		while read -r linea; do
			echo "$linea"
		done < $file | grep '<span id="line221"><\/span>' | sed 's/<span id=\"line221\"><\/span>//g' | sed 's/<span class="attr.*prop<\/span>="//g' | sed 's/<a cl.*lue">\[{//g' | sed 's/<span>//g' | sed 's/<span class="entity">//g' | sed 's/<\/span>//g' | sed 's/&amp//g' | sed 's/;quot;id;quot;:;quot;/\n/g' | sed 's/;quot//g' | sed 's/;,;type[^"]*ption;:;/;/g' | sed 's/;,;likes[^"]*Time;:;/;/g' | sed 's/;,;thumb[^"]*},{//g' | sed 's/;is_video[^"]*<\/a>"//g' > $cleaned_file
	fi
	rm "$file"
done
