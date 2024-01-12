#!/bin/bash

#Data for MySQL
BD_USER='office'
BD_PASS='Kroon111'
BD_NAME='alpha_test' #create a change all_influencers database
BD_HOST='localhost'

"""The system must run as root, if not some programms can't start.
We'll play with the permisions of 1000 user (kroonadmin) and 0 user
(root)"""
if [ "$(id -u)" != "0" ]; then
    echo "Run the system as root"
    exit 1
fi
echo "Running the system as root"

#Create Results folder
if [ ! -d "Results" ]; then
    mkdir "Results"
fi

#Create a database for each .xlsx
"""We need to create a database for each .xlsx, then we can continue
spliting the information"""

actual_directory='./'

db_list_names=()

xlsx_files=($(find "$actual_directory" -maxdepth 1 -name "*.xlsx"))
if [[ ${#xlsx_files} -eq 0 ]]; then 
    echo "The program requires *.xlsx documents"
    exit 1
else
    for file in "${xlsx_files[@]}"; do
        base_name=$(basename "$file" .xlsx)
        db_list_names+=("$base_name")
        echo "Creating a database for $base_name"
        mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" -e "CREATE DATABASE IF NOT EXISTS \`$base_name\`;"
    done
fi

#Creating all_influencers database
"""Creating the database all_influencers, split the information for 
each database in: Companies, Influencers, Mediawaarde, Sticker""" 
python3 split_or_create.py 

#Split.py, we separate the excel and convert everything in a table
python3 split_excel.py "${db_list_names[@]}"

#We will put all the influencers in all_influencers database 


#Extraction process
#We should use all influencers data base
"""In all_influencers data base we have all the influencers of the
all the boxes, at the moment we don't have a system to update or
to detect a change, we only check if we have a data base with the
name of All_influencers and if we don't have it, we'll create"""
result=$(mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" "$BD_NAME" -e "SELECT instagram FROM influencers;")

USER_NAME="kroonadmin"

while read -r instagram; do
    sudo -u $USER_NAME python3 stories.py "$instagram"
done <<< "$result"

echo "Downloading information"

#IA process
"""The IA process is separate in 4 IA's, 1-3 IA's is the IA text
IA_english, IA_dutch, IA_negative. The last IA is the image IA.
For the last IA we need extra steps: check that we have a math 
model for each brand. Fro the maths models we'll need make sense, 
yolov5 and train the model"""
#We need to update the code for the videos, transform frames to
#images and validate it with the diferent IA's
./ia_process.sh

#Split in each box
"""ia_process table has the next columns: id (fk), obj_id (fk)
extract_txt and process. We'll update extract_txt and if it match
with a hashtags in IA process, then we'll update the process. 
The objects without process, we'll move to manual_storage and the
matched objects we'll be separate depence it there are in a colab
or in foody box"""
    #Create folders
        #Colaborations
        """We create colaborations when the nuber of companies in
        companies tables is < 2"""
        #Boxes
        """We create colaborations when the nuber of companies in
        companies tables is > 2"""

#Sent the photos for each folder
"""The boxes are classify in match and no matched, this information 
is in matched table. It'll be attached with ia_process table. This 
process is part of db_excel.py and must be separate in differents parts"""
    #Move matched photos
    """The id_objs in matched table will pass verify the information
    to reach.sh, extract the reach and then insert the info into 
    reach_matched table. Then the objects we'll move for each folder"""

    #Move no matched photos
    """We'll have some folder without match, for this folders we'll
    move manual_storage. An then it will verify manual"""

#Create the excel
"""We'll create a excel with all the info, the code is actually in
db_excel.py, the information that we'll need is: Naam, Datum, Medium,
url/ID, Reach, Mediawaarde. This information is in different data bases.
The objects can be identify with id_obj and we can verify with the ID"""