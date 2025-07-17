import pandas as pd

# rename() function(which let us change index names and/or column names):
reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

x = reviews.rename(columns= {'points': 'score'})
print(reviews.columns)
print(x.columns)  #this will show the changed column points to score