import pandas as pd

# loading our cleaned data
data = pd.read_csv("./data/clean_data.csv")

# explore the data
print data.head()
print data.info()
print data.describe()
