#!/bin/bash

#Data for MySQL
BD_USER='office'
BD_PASS='Kroon111'
BD_NAME='alpha_test'
BD_HOST='localhost'

#Acces as root
if [ "$(id -u)" != "0" ]; then
    echo "Corre como root"
    exit 1
fi

result=$(mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" "$BD_NAME" -e "SELECT instagram FROM influencers;")

USER_NAME="kroonadmin"

while read -r instagram; do
    sudo -u $USER_NAME python3 chat_g.py "$instagram"
done <<< "$result"

./automation.sh