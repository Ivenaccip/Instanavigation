#!/bin/bash

#Data for MySQL
BD_USER='office'
BD_PASS='Kroon111'
BD_NAME='alpha_test'
BD_HOST='localhost'

#Folders
if ! [ -d results ]
    then
        mkdir results
fi

#Comand Line Argument clean
link=$1
link_clean=$(echo "$link" | sed -e 's#https://www.instagram.com/##' | tr -d '/') 
echo "$link_clean"
touch results/reach_$link_clean.txt

#wget y extract
wget --wait=3 --limit-rate=40K -U Mozilla -bq https://www.picnob.com/profile/$link_clean -O results/Ig-$link_clean.txt >/dev/null
sleep 5

if [ ! -s results/Ig-$link_clean.txt ]; then
    echo "El archivo descargado está vacío o no existe."
    exit 1
fi

cat results/Ig-$link_clean.txt | grep '<div class="num"*' | head -2 | tail -1 | sed 's/<div.*tle="//;s/">//g'  >> results/reach_$link_clean.txt


#verificacion de peso
size=$(stat -c%s "results/reach_$link_clean.txt")

# Si el tamaño del archivo es 0, espera 2 segundos más
if [ "$size" -eq 0 ]; then
    echo "Sin peso"
    sleep 1
fi


#Data to DataBase
while read linea; do
    echo "Result $linea"
    linea_sin_comas=$(echo "$linea" | tr -d ',')
    numero_entero=$((linea_sin_comas))

    # Usar numero_entero en tu comando SQL
    mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" "$BD_NAME" -e "INSERT INTO actual_reach (name, reach) VALUES ('$link_clean', $numero_entero);"

done < results/reach_$link_clean.txt