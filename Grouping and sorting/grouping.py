# often we want to group our data, and then do something specific to the group the data is in.

import pandas as pd

data = {
    "store": ['A', 'B', 'A', 'B', 'A', 'B'],
    "sales": [100, 200, 150, 300, 120, 250]
}

df = pd.DataFrame(data)

grouped = df.groupby('store')['sales'].sum()
print(grouped)


reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

#we can use:
print(reviews.points.value_counts())
print()

  #but we also can do:
x = reviews.groupby('points')['points'].count()  #sorts the data also
print(x)


y  = reviews.groupby('points')['price'].min()
print(y)

 ##***
z = reviews.groupby('winery').apply(lambda a : a.title.iloc[0])  #selects the first title for each group
print(z)
print("-------------------")
  #this line could also be done by this-
z = reviews.groupby('winery')['title'].nth(0)
print(z)
