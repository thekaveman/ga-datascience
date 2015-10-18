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

# trying different values of K
for k in range(2,8):
    score = 0
    # simulating the shuffling N times
    N = 10
    for x in range(N):
        # splitting the iris features and target into train and test sets
        features_train, features_test, target_train, target_test = \
            train_test_split(iris_features, iris_target, test_size=0.20)
        # training a KNN classifier
        model = KNeighborsClassifier(k).fit(features_train, target_train)
        # get an accuracy score of the model with this value of k
        score = score + model.score(features_test, target_test)
    # get an average score for these N iterations 
    score = score / N
    print "k = {}, score = {}".format(k, score)
