#!/bin/bash

BD_USER='root'
BD_PASS='Kroon111'
BD_HOST='localhost'

not_for_project=('information_schema' 'mysql' 'performance_schema' 'sys' )

# Obtener la lista de bases de datos
databases=$(mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" -e 'SHOW DATABASES;' | grep -v Database)

# Eliminar las bases de datos que no estén en not_for_project
for db in $databases; do
    if [[ ! " ${not_for_project[@]} " =~ " $db " ]]; then
        echo "Eliminando la base de datos $db"
        mysql -u"$BD_USER" -p"$BD_PASS" -h "$BD_HOST" -e "DROP DATABASE \`$db\`;"
    fi
done