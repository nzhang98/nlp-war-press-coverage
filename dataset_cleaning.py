import pandas as pd
import numpy as np

df = pd.read_csv('/datasets/guardian_dataset_raw.csv', index_col=0).iloc[:,1:]

for i in range(len(df)):
    if df.loc[i, 'newspaperEditionDate'] != df.loc[i, 'newspaperEditionDate']:
        if df.loc[i, 'firstPublicationDate'] != df.loc[i, 'firstPublicationDate']:
            print(i)
        else:
            df.loc[i, 'newspaperEditionDate'] = df.loc[i, 'firstPublicationDate']

for i in range(len(df)):
    if df.loc[i, 'newspaperEditionDate'] != df.loc[i, 'newspaperEditionDate']:
        try:
            df.loc[i, 'newspaperEditionDate'] = df.loc[i-1, 'newspaperEditionDate']
        except Exception:
            print(Exception)
            continue

df = df[['headline', 'bodyText', 'newspaperEditionDate']].rename({'bodyText' : 'body', 'newspaperEditionDate': 'date'}, axis = 1)
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
df.sort_values(['date'], ignore_index=True, inplace=True)

# df.to_csv('/datasets/guardian_dataset_cleaned.csv')