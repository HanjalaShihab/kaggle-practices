import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/winemag-data_first150k.csv')

                     # Native accessors:
# A book object, for example, might have a title property, which we can access by calling book.title.
print(reviews.country)  #just selecting column names
print(reviews.price)

#same thing also for:(If we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:)
print(reviews['country'])
print(reviews['price'])


print(reviews.country[0]) #specifically finding a single value of columns
print(reviews.region_1[5])


