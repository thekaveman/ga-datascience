import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# loading our cleaned data
data = pd.read_csv("./data/clean_data.csv")

# explore the data
print data.head()
print data.info()
print data.describe()

# getting the features and target sets as numpy arrays
passenger_features = data[["Age", "Sex", "Pclass"]].values
passenger_target = data.Survived.values

avg_score = 0
N = 100
k_values = range(2,11)

for k in k_values:
    k_score = 0
    # split and train the model
    for x in range(N):
        # splitting into train/test sets
        features_train, features_test, target_train, target_test = \
            train_test_split(passenger_features, passenger_target, test_size=0.20)
        # building a KNN model
        model = KNeighborsClassifier(k).fit(features_train, target_train)
        # aggregating the score for this value of k
        k_score = k_score + model.score(features_test, target_test)
    # average k_score
    k_score = k_score / N
    # aggregate average
    avg_score = avg_score + k_score
    print "k = {}, k_score = {}".format(k, k_score)

# get the average score of all iterations
avg_score = avg_score / len(k_values)
print "overall avg score = {}".format(avg_score)
