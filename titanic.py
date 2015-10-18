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
