import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

reviews['critic'] = "everyone"  #adding a new column with value "everyone" to the dataset
print(reviews.head())

print(reviews.critic)

print(reviews.shape)