import pandas as pd

df = pd.read_csv('Series-&-Dataframe/winemag-data_first150k.csv')

print(df.head())
print(df.tail(10))

print()

print(df.shape)