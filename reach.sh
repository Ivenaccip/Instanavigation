#!/bin/bash
sudo apt-get install wget -y

#Data for MySQL
BD_USER='office'
BD_PASS='Kroon111'
BD_NAME='alpha_test'
BD_HOST='localhost'

#Folders
if ! [ -d results]
    then
        mkdir results
fi

#wget y extract
wget --wait=20 --limit-rate=40K -U Mozilla -bq https://www.picnob.com/profile/$1/ -O results/Ig-$1.txt >/dev/null
cat results/$1.txt | grep '<div class="num"*' | head -2 | tail -1 >> results/reach_$1.txt

#Data to DataBase
while read linea; do
    reach=$(echo $linea)
    mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" "$BD_NAME" -e "INSERT INTO actual_reach (name, reach) VALUES ('$1', '$reach');"
done < results/$1.txt