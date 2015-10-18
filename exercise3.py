import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# reading in the training preparing training data
trainingData = pd.read_csv("./data/clean_data.csv")

# getting the features and target sets as numpy arrays
passenger_features = trainingData[["Age", "Sex", "Pclass"]].values
passenger_target = trainingData.Survived.values

# creating a random forest classifier with training data
model = RandomForestClassifier().fit(passenger_features, passenger_target)
