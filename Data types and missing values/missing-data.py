import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

x = reviews[pd.isnull(reviews.country)]
print(x)
print("-------------------")

#same as:
y = reviews.loc[reviews.country.isnull()]
print(y)

#not necesary:
sorted = reviews.sort_index(ascending= True)
print(sorted)
print("-------------------")


#Replacing missing values:
z = reviews.region_2.fillna("Unknown")
