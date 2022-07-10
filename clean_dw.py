
import pandas as pd
import numpy as np

from secret import cnxn

df_fatal = pd.read_sql("SELECT * FROM [Fatal_Police_Shooting]", cnxn)

df_fatal = df_fatal.drop(columns=["is_geocoding_exact", "body_camera"])

df_fatal['date'].isnull().sum()

df_fatal['age'].isnull().sum()

df_fatal['age'] = df_fatal['age'].fillna(0)

df_fatal['age'].isnull().sum()

df_fatal['longitude'].isnull().sum()

df_fatal['longitude'] = df_fatal['longitude'].fillna(0)

df_fatal['longitude'].isnull().sum()

df_fatal['latitude'].isnull().sum()

df_fatal['latitude'] = df_fatal['latitude'].fillna(0)

df_fatal['latitude'].isnull().sum()

df_fatal['name'] = df_fatal['name'].replace(np.nan, "undetermined")

df_fatal['name'].isnull().sum()

df_fatal['manner_of_death'].isnull().sum()

df_fatal['armed'].isnull().sum()

df_fatal['armed'] = df_fatal['armed'].replace(np.nan, "undetermined")

df_fatal['armed'].isnull().sum()

df_fatal['gender'].isnull().sum()

df_fatal['gender'] = df_fatal['gender'].replace(np.nan, "undetermined")

df_fatal['gender'].isnull().sum()

df_fatal['race'].isnull().sum()

df_fatal['race'] = df_fatal['race'].replace('None', "undetermined")

df_fatal['race'] = df_fatal['race'].replace('N', "undetermined")

df_fatal['race'] = df_fatal['race'].replace('O', "undetermined")

df_fatal['race'].isnull().sum()

df_fatal['city'].isnull().sum()

df_fatal['state'].isnull().sum()

df_fatal['signs_of_mental_illness'].isnull().sum()

df_fatal['threat_level'].isnull().sum()

df_fatal['flee'].isnull().sum()

df_fatal['flee'] = df_fatal['flee'].replace(np.nan, "undetermined")

df_fatal['flee'].isnull().sum()



df_us_cities = pd.read_sql("SELECT * FROM [us_cities]", cnxn)

df_us_cities.isnull().sum().sum()

df_us_cities['zips'] = df_us_cities['zips'].fillna(0)

df_us_cities = df_us_cities.drop(columns=["military", "timezone", "incorporated", "source", "ranking", "city_ascii", "state_id", "county_name_all", "county_fips_all"])

df_Etnicity = pd.read_sql("SELECT * FROM [Etnicity]", cnxn)

df_Etnicity.isnull().sum().sum()


from secret import cndw

df_fatal.to_sql("df_fatal", cndw , schema=None, if_exists='replace', index=True, index_label= None, chunksize = None , dtype = None , method = None)
df_us_cities.to_sql("df_us_cities", cndw , schema=None, if_exists='replace', index=True, index_label= None, chunksize = None , dtype = None , method = None)
df_Etnicity.to_sql("df_Etnicity", cndw , schema=None, if_exists='replace', index=True, index_label= None, chunksize = None , dtype = None , method = None)

