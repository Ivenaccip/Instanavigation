#!/bin/bash

#Data for MySQL
BD_USER='root'
BD_PASS='Kroon111'
BD_NAME='alpha_test' #create a change all_influencers database
BD_HOST='localhost'

#Create a database for each .xlsx
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
        mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" -e "GRANT INSERT ON \`$base_name\`.* TO '$BD_USER'@'$BD_HOST';"
    done
    mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" -e "FLUSH PRIVILEGES;"
fi

python3 split_or_create.py 

python3 split_excel.py "${db_list_names[@]}"