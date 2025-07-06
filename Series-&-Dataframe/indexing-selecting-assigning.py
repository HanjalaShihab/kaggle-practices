import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/winemag-data_first150k.csv')

                     # Native accessors:
# A book object, for example, might have a title property, which we can access by calling book.title.
print(reviews.country)  #just selecting column names
print(reviews.price)


#same thing also for:(If we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:)
print(reviews['country'])
print(reviews['price'])


print(reviews.country[0]) #specifically finding a single value of columns
print(reviews.region_1[5])

#or we could also do this:
print(reviews['country'][10])
print(reviews['region_1'][: 10])  #can explicitly print multiple values also!!!!



#Indexing in pandas: (pandas has its own accessor operators, loc and iloc)
                    #indexing based selection:
print(reviews.iloc[0])  #Selecting the first row   (Both loc and iloc are row-first, column-second)

#This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns.
# To get a column with iloc, we can do the following:
print(reviews.iloc[:, 1]) #all rows then first column
print(reviews.iloc[:3, 1])

#we can pass list also:
print(reviews.iloc[[1,2,3,4,5], 5])

#negative indexing:
print(reviews.iloc[-5:])  #last 5 rows with all columns

               #level based selection:
print(reviews.loc[0, 'country'])
print(reviews.loc[:, ['variety', 'winery', 'points']])

print(reviews.iloc[:3, :])  #first 3 rows and all columns
