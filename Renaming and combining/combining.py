import pandas as pd

#lets say we have two datasets.And we want to combine them into a single dataset:

#firstly we have to read the csv files:

first_one = pd.read_csv("Series-&-Dataframe/winemag-data_first150k.csv")
second_one = pd.read_csv("Series-&-Dataframe/manipulate index/winemag-data-130k-v2.csv")

