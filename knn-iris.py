import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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

# splitting the iris features and target into train and test sets
features_train, features_test, target_train, target_test = \
    train_test_split(iris_features, iris_target, test_size=0.20, random_state=0)

# training a KNN classifier
model = KNeighborsClassifier(3).fit(features_train, target_train)

# now make predictions on probabilities
print model.predict_proba(features_test)

# compare predictions with the truth data
print model.predict(features_test)
print target_test

# get an accuracy score of the model
print model.score(features_test, target_test)
