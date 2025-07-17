import pandas as pd

# rename() function(which let us change index names and/or column names):
reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

reviews = reviews.rename(columns= {'points': 'score'})
print("--------------------------")
print(reviews.columns)
print("--------------------------")


#renaming another column:
reviews = reviews.rename(columns= {'region_1': 'first_region', 'region_2': 'second_region'})
print(reviews.columns)
print("--------------------------")


#renaming index:
z = reviews.rename(index= {
    0: 'firstEntry',
    1 : 'secondEntry'
})
print(z)   #renaming index values are very rare.For that set_index() function is usually more convenient.
print("--------------------------")


reviews = reviews.set_index("title")  #setting the title column as the index column
print(reviews)
print("--------------------------")


x = reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(x)