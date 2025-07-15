import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

#use of dtype property:
print(reviews['price'].dtype)
print("-------------------")

print(reviews.dtypes)
print("-------------------")


#It's possible to convert a column of one type into another wherever such a conversion makes sense by using the astype() function.
x = reviews.points.astype('float64')
print(x)
print("-------------------")


# a dataframe or series index has it's own dtype too:
print(reviews.index.dtype)
print("-------------------")


#recalling:
print(reviews.country.isnull())  #will return the country column only(True, false)
#but to retrive the rows where country is not given:
print(reviews.loc[reviews['country'].isnull()])