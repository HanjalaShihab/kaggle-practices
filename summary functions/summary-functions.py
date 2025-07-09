#Pandas provides many simple "summary functions" (not an official name)
#     which restructure the data in some useful way.

import pandas as pd

reviews = pd.read_csv('summary functions/winemag-data-130k-v2.csv')

# describe method():

print(reviews.points.describe())
print()
print(reviews.price.describe())
print()