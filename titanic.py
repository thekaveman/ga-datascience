import pandas as pd

# import the titanic data into DataFrame
data = pd.read_csv("./data/train.csv")

# view the first N rows
print data.head(10)

# view the last N rows
print data.tail(10)

# investigate the data types in the DataFrame
print data.info()

# get some summary stats
print data.describe()

# transpose the result
print data.describe().T

# filtering for a column value
onlyMen = data[data.Sex == "male"]
print onlyMen

# filtering a specific column based on another column's value
onlyMenAges = data.Age[data.Sex == "male"]
print onlyMenAges

# filter a couple columns based on another column's value
onlyMenAgesNames = data[["Age", "Name"]][data.Sex == "male"]
print onlyMenAgesNames

# count the men and women
print data.Sex[data.Sex == "male"].count()
print data.Sex[data.Sex == "female"].count()

# calc the survival rate for adult men (age >= 18)
adultMenSurvivalRate = \
    data.Survived[(data.Sex == "male") & (data.Age >= 18)].mean()
print adultMenSurvivalRate

# calc the survival rate for women and children
womenChildrenSurvivalRate = \
    data.Survived[(data.Sex == "female") | (data.Age < 18)].mean()
print womenChildrenSurvivalRate
