import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')  #another dataset

print(reviews.head())
print(reviews.shape)


#we can set the title column as the index column:
x = reviews.set_index("title")
print(x)


                               #Conditional selection:
print(reviews.country == "Italy")   #returns true for country Italy in every row


#printing all the rows where country is Italy:
print(reviews.loc[reviews.country == "Italy"])


print(reviews.iloc[0])


                               #Conditional selection:
print(reviews.country == "Italy")   #returns true for country Italy in every row


#printing all the rows where country is Italy:
print(reviews.loc[reviews.country == "Italy"])


print(reviews.iloc[0])    #to see all the column names as it couldn't be seen with native accessors

   #now multiple conditional selection:
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points > 80)])

print(reviews.loc[reviews.price == 85].head())

print(reviews.loc[(reviews.country == 'US') | (reviews.price == 100)].head())


#Pandas comes with a few built-in conditional selectors, two of which we will highlight here.

#The first is isin. isin is lets you select data whose value "is in" a list of values.
#          For example, here's how we can use it to select wines only from Italy or France:

print(reviews.loc[reviews.country.isin(['US', 'Germany'])])  #like what if there are multiple countries we want?

print(reviews.loc[reviews.country.isin(['Germany', 'France'])])

#The second is isnull (and its companion notnull). 
# These methods let you highlight values which are (or are not) empty (NaN). 
# For example, to filter out wines lacking a price tag in the dataset, here's what we would do:

