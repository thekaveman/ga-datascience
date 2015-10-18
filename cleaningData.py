import pandas as pd

# import the titanic data into DataFrame
data = pd.read_csv("./data/train.csv")

# what does the data look like before filling?
print data.info()

# fill with the average age (overwriting the current Age column)
avg_age = data.Age.mean()
data.Age = data.Age.fillna(avg_age)

# look at the data again after filling to ensure it didn't significant alter
print data.info()

# replace text with boolean in Sex column
data.Sex = data.Sex.replace(["male", "female"],
                            [True, False])

# ensure the replacement worked
data.head(20)
