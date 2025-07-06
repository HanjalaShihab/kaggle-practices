import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/winemag-data_first150k.csv')

# Native accessors:
print(reviews.country)
print()


print(reviews.country[0])