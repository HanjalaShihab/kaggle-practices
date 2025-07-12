import pandas as pd

reviews = pd.read_csv('summary functions/winemag-data-130k-v2.csv')

#A map is a term, borrowed from mathematics, for a function that takes 
 #one set of values and "maps" them to another set of values.

 #In data science we often have a need for creating new 
 # representations from existing data, or for transforming 
 # data from the format it is in now to the format that we want it to be in later. 
 # Maps are what handle this work

x = lambda a : a + 10  #recalling lambda function of pys
print(x(5))    
print()


#suppose that we want to remean the scores the wines received to 0:

review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p : p - review_points_mean))
print()

print(reviews.points.head())  # checking if the dataframe has changed for points column
print()

#in the above example refers to: (every value of point column - point column mean)

   # apply() function is the equivalent method if we want to transform a whole
   # Dataframe by calling a custom method on each row:

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews_remeaned = reviews.apply(remean_points, axis = 'columns')
print(reviews_remeaned.points)


#Note that map() and apply() return new, transformed Series and DataFrames, respectively. 
#They don't modify the original data they're called on. 