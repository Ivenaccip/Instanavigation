from sqlalchemy import create_engine

"""
This code was made to create the data base all_influencers
First, it'll verify if the table all_influencers exists, if
the table exist, then we'll split the database information
in: Influencers, Sticker, Companies, Mediawaarde 
"""
# Checking if the database 'all_influencers' exists
# Parametros to connect to the database
user= 'office'
password= 'Kroon111'
host= 'localhost'

chain_conection= f'mysql+mysqlconnector://{user}:{password}@{host}/'

#Create a motor
engine = create_engine(chain_conection)

#Create the database if it doesnt exist
with engine.connect() as cursor:
    cursor.execute('CREATE DATABASE IF NOT EXISTS all_influencers')
    cursor.execute('USE all_influencers')
    cursor.execute('CREATE TABLE IF NOT EXISTS all_influencers (influencer VARCHAR(255), link TEXT, boxes TEXT)')

engine.dispose()
chain_bd= f'mysql+mysqlconnector://{user}:{password}@{host}/all_influencers'
engine = create_engine(chain_conection)

#Conection to fill the database
not_for_project = ['information_schema', 'mysql', 'performance_schema', 'sys', 'all_influencers']
with engine.connect() as conn:
    result = conn.execute("SHOW DATABASES;")
    data_bases = [ db[0] for db in result if db[0] not in not_for_project ]

#Check databases
for i in data_bases:
    print(i)