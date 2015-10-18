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

# create an Excel file with the names and ages of the survivors on one tab...
# ...and the names and ages of the deceased on another tab
writer = pd.ExcelWriter("./data/titanic.xlsx")

survivors = data[["Name", "Age"]][data.Survived == 1]
deceased = data[["Name", "Age"]][data.Survived == 0]

survivors.to_excel(writer, "Survivors")
deceased.to_excel(writer, "Deceased")

writer.save()
