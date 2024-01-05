#!/bin/bash

# Show the boxes
show_boxes() {
    # Read all .xlsx files into an array, except those starting with "Results"
    files=()
    while IFS= read -r -d $'\0' file; do
        files+=("$file")
    done < <(find . -type f -name "*.xlsx" ! -name "Results*.xlsx" -print0)

    num_files=${#files[@]} # Number of files

    echo
    echo "                                     ==============================="

    # If there are more than 5 files, show a message and don't list the files
    if [ "$num_files" -gt 5 ]; then
        echo " There are too many boxes, please erase a box or contact Leo"
    else
        # Display files depending on how many we have
        for (( idx=0; idx<num_files; idx++ )); do
            printf "                                     [%d]          %s \n" $((idx+1)) "${files[idx]##*/} |"
        done
    fi

    echo "                                     [x]   ------> Exit <------   |"
    echo "                                     ==============================="
    echo
}

# Check if MySQL is activate
mysql_on() {
    if systemctl is-active --quiet mysql; then
        echo "MySQL service is active."
    else
        echo "The MySQL service is not active. Do you want to turn on the service?"
        read -p " [ C ] Accept | [ X ] Decline: " turnon_mysql
        case $turnon_mysql in
            [Cc])
                echo "Attempting to start MySQL service..."
                sudo systemctl start mysql
                if systemctl is-active --quiet mysql; then
                    echo "MySQL service started successfully."
                else
                    echo "Failed to start MySQL service."
                fi
                ;;
            [Xx])
                echo "Exiting without starting MySQL service."
                ;;
            *)
                echo "Invalid option."
                ;;
        esac
    fi
}

# Verify Database
check_database() {
    db_name="$1"
    echo "Verifying if the database exists: $db_name"

    # Comando para verificar la existencia de la base de datos
    # Asegúrate de reemplazar las credenciales con las tuyas
    if mysql -u "your_mysql_username" -p"your_mysql_password" -e "use $db_name;" 2>/dev/null; then
        echo "The database '$db_name' is ready."
    else
        echo "The database '$db_name' wasn't found." 
        echo "Do you want to create a database?"
        read -p " [ C ] Yes | [ X ] No: " split_excel
        case $split_excel in
            [Cc])
                echo "Creating database '$db_name'..."
                mysql -u "your_mysql_username" -p"your_mysql_password" -e "CREATE DATABASE $db_name;"
                ;;
            [Xx])
                echo "Exiting without creating database."
                ;;
            *)
                echo "Invalid option."
                ;;
        esac
    fi
}

clear
echo
echo "                         .-------..-------..-------..-------..------.     .-------..-------. "
echo "                         |K.---. ||R.---. ||O.---. ||O.---. ||N.---. |    |I.---. ||A.---. | "
echo "                         | :/ \: || :( ): || :/ \: || :/ \: || :( ): |    | :\ /: || :\ /: | "
echo "                         | :/K\: || :(R): || :/O\: || :/O\: || :(N): |    | :(I): || :(A): | "
echo "                         | :\ /: || :( ): || :\ /: || :\ /: || :( ): |    | :\ /: || :\ /: | "
echo "                         | '---'K|| '---'R|| '---'O|| '---'O|| '---'N|    | '---'I|| '---'A| "
echo "                         '-------''-------''-------''-------''-------'    '-------''-------' "
echo "                                    🔍 Instagram   Posts  and   Stories 🔍      "
echo "                         ____________________________________________________________________"					
echo "                               ︻デ═一  Created by: Ivenaccip  v.Alpha α  一═デ︻ " 
echo "          ---------------------------------------------------------------------------------------------"
echo "                      Automatisering van kunstmatige intelligentie van 'Kroon Op Het Werk'"
echo "          ---------------------------------------------------------------------------------------------"
echo
echo
echo "                                     ==============================="
echo "                                     [1]       Collaborations 🤝""    |"
echo "                                                                    |"
echo "                                     [2]         Influencers 😎""     |"
echo "                                                                    |"
echo "                                     [3]          Process 🔃""        |"
echo "                                                                    |"
echo "                                     [x]   ------> Exit ""<------   |"
echo "                                     ==============================="
echo
while true
do
    read -p "[*] Select an option: " opc1
        case $opc1 in
            1)  clear
                echo ""
                echo "                         .-------..-------..-------..-------..------.     .-------..-------. "
                echo "                         |K.---. ||R.---. ||O.---. ||O.---. ||N.---. |    |I.---. ||A.---. | "
                echo "                         | :/ \: || :( ): || :/ \: || :/ \: || :( ): |    | :\ /: || :\ /: | "
                echo "                         | :/K\: || :(R): || :/O\: || :/O\: || :(N): |    | :(I): || :(A): | "
                echo "                         | :\ /: || :( ): || :\ /: || :\ /: || :( ): |    | :\ /: || :\ /: | "
                echo "                         | '---'K|| '---'R|| '---'O|| '---'O|| '---'N|    | '---'I|| '---'A| "
                echo "                         '-------''-------''-------''-------''-------'    '-------''-------' "
                echo "                                    🔍 Instagram   Posts  and   Stories 🔍      "
                echo "                         ____________________________________________________________________"					
                echo "                               ︻デ═一  Created by: Ivenaccip  v.Alpha α  一═デ︻ " 
                echo "          ---------------------------------------------------------------------------------------------"
                echo "                      Automatisering van kunstmatige intelligentie van 'Kroon Op Het Werk'"
                echo "          ---------------------------------------------------------------------------------------------"
                echo
                show_boxes
                read -p "Select a file: " file_number
                if [[ $file_number -ge 1 ]] && [[ $file_number -le 5 ]]; then
                    if [ $file_number -le $num_files ]; then
                        file_name="${files[$file_number-1]##*/}"
                        db_name="${file_name%.*}"  # Extrae el nombre base del archivo
                        mysql_on
                        check_database "$db_name"
                    else
                        echo "Invalid selection."
                    fi
                else
                    echo "Please select a valid box"
                fi
                ;;
            x) 
                echo "Exit"
                exit 0
                ;;
            *)
                echo "Option no enable"
                ;;
            
        esac
done