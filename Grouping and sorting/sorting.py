import pandas as pd

reviews = pd.read_csv('Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv')

print(reviews.columns)
print("----------------------------")


countries_reviewed = reviews.groupby(['country', 'province'])['points'].agg(max)
print(countries_reviewed)
print("----------------------------")


x = countries_reviewed.index
print(type(x))
print("----------------------------")


          #sorting starting here:
# first we have to normalize or Make the dataset  RangeIndex again:
countries_reviewed = countries_reviewed.reset_index()

sorted = countries_reviewed.sort_values(by= 'points')
print(sorted)
print("----------------------------")



#Sort by Row Count Per Group:
countries_reviewed = reviews.groupby(['country', 'province']).size().reset_index(name= 'len')
sorted = countries_reviewed.sort_values(by= 'len', ascending= False)
print(sorted)
print("----------------------------")


# To sort by index values:
sorted = countries_reviewed.sort_index()
#print(sorted.to_string())  to see the full dataframe
print(sorted)
print("----------------------------")


#We can also sort by more than one column at a time:
y = countries_reviewed.sort_values(by= ['country', 'len'], ascending= True)  #ascending among the groups of lens for countries not whole len
print(y)
print("----------------------------")
