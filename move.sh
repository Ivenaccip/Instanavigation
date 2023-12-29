#!/bin/bash

#Data for MySQL
BD_USER='office'
BD_PASS='Kroon111'
BD_NAME='alpha_test'
BD_HOST='localhost'

# Define vars
user="kroonadmin"
origin="/home/${user}/Downloads"
destination=$(pwd)

# actual date in format
today=$(date +"%Y-%m-%d")

# Create a folter with the date | Inside of destination
destination_folder="${destination}/${today}"

# We're gonna modify the image and update the info
process_image() {

    local imagen=$1
    local pross_applied=$2
    local language=$3

    # Extract the name from the file without the extension
    if [[ $language == "eng" ]]; then
        local nombre_base=$(basename "$imagen" .jpeg)
    else
        local nombre_base="dutch_$(basename "$imagen" .jpeg)"
    fi

    # Use Tesseract to convert the image to text
    tesseract "$imagen" "${destination_folder}/${nombre_base}_texto" -l $language

    echo "Extract text from $imagen , save in ${nombre_base}_texto .txt"

    # Read content of the file to text
    extract_text=$(<"${destination_folder}/${nombre_base}_texto.txt" | tr '\n' ' ')

    # Solution for SQL consults
    extract_text=$(printf '%s' "$extract_text" | sed "s/'/''/g;")

    # Update info if process = eng != insert into
    if [[ $pross_applied == "ENG" ]]; then
        mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" "$BD_NAME" -e "
            UPDATE id_obj_download SET Extract_text='$extract_text', Process='$pross_applied' WHERE Object_ID='$nombre_base';
        "
    elif [[ $pross_applied == "DUT" ]] || [[ $pross_applied == "NEG" ]]; then
        # Duplicamos la informacion
        info=$(mysql -u "$BD_USER" -p "$BD_PASS" -h "$BD_HOST" "$BD_NAME" -sN -e "
            SELECT Type, Link, Extract_text, Fecha, Profile, Process FROM id_obj_download WHERE Object_ID = $
        ")
        # Insertamos la informacion
        mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" "$BD_NAME" -e "
            INSERT INTO id_obj_download (Object_ID, Type, Link) VALUES ($nombre_base, "PI", );
        "
    else
        echo "Error in the update or in the upload process"
    fi
}

mkdir -p "${destination_folder}"

# Move the files .jpeg from the origin to the destiny folder with the date of today
mv "${origin}"/*.jpeg "${destination_folder}/"

#English
for image in "${destination_folder}"/*.jpeg; do
    if [[ -f "$image" ]]; then
        process_image "$image" "ENG" "eng"
    fi
done 

#Dutch
for image in "${destination_folder}"/*.jpeg; do
    if [[ -f "$image" ]]; then
        process_image "$image" "DUT" "nld"
    fi
done 

#Negative Process
python3 negative.py "$today"

#Same process, but this time in negative
for image in "${destination_folder}"/*_negative.jpeg; do
    if [[ -f "$image" ]]; then
        process_image "$image" "NEG" "eng"
    fi
done 