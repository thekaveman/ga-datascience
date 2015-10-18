import pandas as pd

# import the titanic data into DataFrame
data = pd.read_csv("./data/train.csv")

# what was the average age of the survivors?

avgSurvivalAge = data["Age"].mean()
print avgSurvivalAge

# what was the survival rate of the children and seniors?

surivalRateChildrenSeniors = \
    data.Survived[(data.Age < 18) | (data.Age > 60)].mean()
print surivalRateChildrenSeniors

# group by Pclass and investigate average survival rate, age and fare
groupedByPclass = data.groupby("Pclass")
print groupedByPclass.describe().T
