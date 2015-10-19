import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# reading and preparing training data
trainingData = pd.read_csv("./data/clean_data.csv")
passenger_features = trainingData[["Age", "Sex", "Pclass"]].values
passenger_target = trainingData.Survived.values

# creating a random forest classifier with training data
model = RandomForestClassifier().fit(passenger_features, passenger_target)

# reading and preparing test data
testData = pd.read_csv("./data/test.csv")
testData.Age = testData.Age.fillna(testData.Age.mean())
testData.Sex = testData.Sex.replace(["male", "female"], [True, False])

# predicting outcomes using test data
features = testData[["Age", "Sex", "Pclass"]].values
predictions = model.predict(features)
testData["Survived"] = predictions

# create a csv for uploading to Kaggle
kaggle = testData[["PassengerId", "Survived"]]
kaggle.to_csv("./data/kaggle.csv", header=True, index=False)
