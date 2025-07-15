import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

countries_reviewed = reviews.groupby(['country', 'province'])['points'].agg(max)
print(countries_reviewed)
print("----------------------------")


x = countries_reviewed.index
print(type(x))