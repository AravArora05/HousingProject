import pandas as pd

df = pd.read_csv('ZHVI.csv')

df = df.dropna()

df = df.transpose()

df['Region'] = [None, 'Southeast', 'West', 'Southeast', 'Northeast', 'Southwest', 'Northeast', 'West', 'Northeast', 'West', 'Southwest', 'West', 'Southeast', 'Southeast', 'West', 'Midwest', 'West', 'West', 'Midwest', 'Southeast', 'Midwest', 'Southeast', 'Southeast', 'Northeast', 'Midwest', 'Northeast', 'Midwest', 'Midwest', 'Northeast', 'Northeast', 'Midwest', 'West', 'West', 'Northeast', 'Southwest', 'Southeast', 'Northeast', 'Southeast', 'Northeast', 'Midwest', 'Midwest', 'Midwest', 'West', 'Midwest', 'Midwest', 'Southeast', 'Southwest', 'Southeast', 'West', 'Southeast', 'Southeast', 'Northeast']

df.to_csv('modified_ZHVI.csv', index=False)