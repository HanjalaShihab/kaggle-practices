import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

print(reviews.columns)
print("----------------------------")


countries_reviewed = reviews.groupby(['country', 'province'])['points'].agg(max)
print(countries_reviewed)
print("----------------------------")


x = countries_reviewed.index
print(type(x))
print("----------------------------")


          #sorting starting here:
# first we have to normalize or Make the dataset  RangeIndex again:
countries_reviewed = countries_reviewed.reset_index()

sorted = countries_reviewed.sort_values(by= 'points')
print(sorted)
