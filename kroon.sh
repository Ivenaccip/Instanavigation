#!/bin/bash

# Show the boxes
show_boxes() {
    # Search all the files which ends with .xlsx and don't start with "Results". All this information will go to an array
    IFS=$'\n' read -r -d '' -a files < <(find . -type f -name "*.xlsx" ! -name "Results*.xlsx" -print0)
    num_files=${#files[@]} # Get the number of files

    echo
    echo "                                     ==============================="

    # If there are more than 5 files, show the message and don't list the files
    if [ "$num_files" -gt 5 ]; then
        echo " There are so many boxes, please erase a box or contact Leo"
    else
        # Check how many file do we have and change the options
        case $num_files in
            1)
                echo "                                                                                                              "
                echo "                                                                                                              "
                printf "                                     [1]          %s \n" "${files[0]##*/}"
                echo "                                                                                                              "
                echo "                                                                                                              "                
                echo "                                                                                                              "
                ;;
            2)
                echo "                                                                                                              "
                echo "                                                                                                              "
                printf "                                     [1]          %s \n" "${files[0]##*/}"
                echo "                                                                                                              "
                printf "                                     [2]          %s \n" "${files[1]##*/}"
                echo "                                                                                                              "
                ;;
            3)
                echo "                                                                                                              "
                printf "                                     [1]          %s \n" "${files[0]##*/}"
                echo "                                                                                                              "
                printf "                                     [2]          %s \n" "${files[1]##*/}"
                echo "                                                                                                              "
                printf "                                     [3]          %s \n" "${files[2]##*/}"
                echo "                                                                                                              "
                ;;
            4)
                printf "                                     [1]          %s \n" "${files[0]##*/}"
                printf "                                     [2]          %s \n" "${files[1]##*/}"
                echo "                                                                                                              "
                echo "                                                                                                              "
                printf "                                     [3]          %s \n" "${files[2]##*/}"
                printf "                                     [4]          %s \n" "${files[3]##*/}"
                ;;
            5)
                printf "                                     [1]          %s \n" "${files[0]##*/}"
                printf "                                     [2]          %s \n" "${files[1]##*/}"
                printf "                                     [3]          %s \n" "${files[2]##*/}"
                printf "                                     [4]          %s \n" "${files[3]##*/}"
                printf "                                     [5]          %s \n" "${files[4]##*/}"
                echo "                                                                                                              "
                ;;
            *)
                for ((idx=0; idx<num_files; idx++)); do
                    printf "                                     [%d]          %s \n" $((idx+1)) "${files[idx]##*/}"
                    echo "                                                                                                              "
                done
                ;;
        esac
    fi

    echo "                                     [Esc]   ------> Exit <------   |"
    echo "                                     ==============================="
    echo
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
echo "                               ︻デ═一   Created by: Ivenaccip  v.Alpha α ︻デ═一 " 
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
echo "                                     [Esc]   ------> Exit ""<------   |"
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
                echo "                               ︻デ═一   Created by: Ivenaccip  v.Alpha α ︻デ═一 " 
                echo "          ---------------------------------------------------------------------------------------------"
                echo "                      Automatisering van kunstmatige intelligentie van 'Kroon Op Het Werk'"
                echo "          ---------------------------------------------------------------------------------------------"
                echo
                show_boxes
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