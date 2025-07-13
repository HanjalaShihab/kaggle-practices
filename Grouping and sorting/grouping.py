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
z = reviews.groupby('winery')['title'].nth(0)  #this is different then the other two
print(z)
print("--------------------")
#and
z = reviews.groupby('winery')['title'].agg('first')
print(z)
print("------------------")

# can also group by more than one column. For an example,
#  here's how we would pick out the best wine by country and province:
data = reviews.groupby(['country', 'province']).apply(lambda a : a.loc[a.points.idxmax()])
print(data)
print("--------------")

NaNRemoved = reviews.dropna(subset=['price'])
data = NaNRemoved.groupby(['country','province']).apply(lambda df : df.loc[df.price.idxmax()])