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

#Create Retults folder

#Split and all_influencers data base
"""Verify if we have a database for each .xlsx
If we don't have, we'll run split.py
If it exist, we will verify all_influencers data base""" 
    #Split.py, we separate the excel and convert everything in a table

    #We will create all_influencers data base

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