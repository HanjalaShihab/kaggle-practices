import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

x = reviews[pd.isnull(reviews.country)]
print(x)

sorted = reviews.sort_index(ascending= True)
print(sorted)