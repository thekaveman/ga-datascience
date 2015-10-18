import pandas as pd

# import the iris dataset into a DataFrame
iris = pd.read_csv("./data/iris.csv")

# exploring the data
print iris.head()
print iris.info()
print iris.describe()

# create two variables, for features and target -> convert to values
iris_features = iris[["sepal_length",
                      "sepal_width",
                      "petal_length",
                      "petal_width"]].values

iris_target = iris.species.values
