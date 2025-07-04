import pandas as pd

df = pd.read_csv('Series-&-Dataframe/winemag-data_first150k.csv')

print(df.shape)   #returns the number of rows(150930) and columns(11)
print()
#

print(df.info())
print()
#

print(df.head())
print()
#

print(df.tail())
print()
#