import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

x = reviews[pd.isnull(reviews.country)]
print(x)
print("-------------------")

#same as:
y = reviews.loc[reviews.country.isnull()]
print(y)

#not necesary:
sorted = reviews.sort_index(ascending= True)
print(sorted)
print("-------------------")


#Replacing missing values:
reviews.region_2.fillna("Unknown", inplace=True)   #this is not a good practice for using inplace parameter
print(reviews['region_2'])
print("-------------------")


#the good practice for replacing values for the above example is:
reviews.fillna({'region_2': 'Hanjala'}, inplace= True)  #This won't override the "Unknown as they are already filled"
print(reviews['region_2'])
print("-------------------")


#We can replace the "Unknowns":
reviews['region_2'] =reviews['region_2'].replace("Unknown", "Hanjala")
print(reviews['region_2'])