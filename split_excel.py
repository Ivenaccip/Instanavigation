import pandas as pd
from sqlalchemy import create_engine

file_excel = 'X-mas.xlsx'

companies = 'Companies'
influencers = 'Influencers'
mediawaarde = 'Mediawaarde'
phrase = 'Sticker'

user = 'office'
password = 'Kroon111'
host = 'localhost'
bd = 'alpha_test'
chain_conection = f'mysql+mysqlconnector://{user}:{password}@{host}/{bd}'

engine = create_engine(chain_conection)

df = pd.read_excel(file_excel, sheet_name=companies)
df_influencers = pd.read_excel(file_excel, sheet_name=influencers)
df_media = pd.read_excel(file_excel, sheet_name=mediawaarde)
df_phrase = pd.read_excel(file_excel, sheet_name=phrase)

#rewrite columns in order to match with the tables of the database
df_media.rename(columns={'Van': 'van', 'Tot volgers': 'tot', 'Bedrag': 'bedrag'}, inplace=True)

df.to_sql('companies', con=engine, if_exists='append', index=False)
df_influencers.to_sql('influencers', con=engine, if_exists='append', index=False)
df_media.to_sql('mediawaarde', con=engine, if_exists='append', index=False)
df_phrase.to_sql('sticker', con=engine, if_exists='append', index=False)
