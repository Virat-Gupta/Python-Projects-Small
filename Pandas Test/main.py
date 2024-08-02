import pandas

data = pandas.read_csv("Pandas Test\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240731.csv")

print(data["Primary Fur Color"].value_counts())
