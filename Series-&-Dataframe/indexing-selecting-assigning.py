import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/winemag-data_first150k.csv')

# Native accessors:
print(reviews.country)  #just selecting column names
print(reviews.price)


print(reviews.country[0]) #specifically finding a single value of column
print(reviews.region_1[5])

