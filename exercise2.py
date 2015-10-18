import pandas as pd
from sklearn.cross_validation import train_test_split

# loading our cleaned data
data = pd.read_csv("./data/clean_data.csv")

# explore the data
print data.head()
print data.info()
print data.describe()

# getting the features and target sets as numpy arrays
passenger_features = data[["Age", "Sex", "Pclass"]].values
passenger_target = data.Survived.values

# splitting into train/test sets
features_train, features_test, target_train, target_test = \
    train_test_split(passenger_features, passenger_target, test_size=0.20)
