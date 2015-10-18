import pandas as pd

# import the titanic data into DataFrame
data = pd.read_csv("./data/train.csv")

# what was the average age of the survivors?

avgSurvivalAge = data["Age"].mean()
print avgSurvivalAge
