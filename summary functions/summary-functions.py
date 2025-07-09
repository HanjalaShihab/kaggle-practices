#Pandas provides many simple "summary functions" (not an official name)
#     which restructure the data in some useful way.

import pandas as pd

reviews = pd.read_csv('summary functions/winemag-data-130k-v2.csv')

print(reviews.head())
# describe method():

print(reviews.points.describe())
print()
print(reviews.price.describe())
print()
print(reviews.taster_twitter_handle.describe())
print()

#we can use mean(), median() and mode() funcitons:
print(reviews.points.mean())
print()


Summary functions
Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way. For example, consider the describe() method:

reviews.points.describe()
count    129971.000000
mean         88.447138
             ...      
75%          91.000000
max         100.000000
Name: points, Length: 8, dtype: float64
This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output changes based on the data type of the input. The output above only makes sense for numerical data; for string data here's what we get:

