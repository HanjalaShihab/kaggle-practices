import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')  #another dataset

print(reviews.head())
print(reviews.shape)


#we can set the title column as the index column:
x = reviews.set_index("title")

print(x)