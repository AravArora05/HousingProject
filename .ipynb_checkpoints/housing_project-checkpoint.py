import pandas as pd

df = pd.read_csv('ZHVI.csv')

df = df.dropna()

df.to_csv('modified_ZHVI.csv', index=False)

print(df)

