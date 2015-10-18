import pandas as pd

# loading DataFrame from a CSV file

data = pd.read_csv("./data/test_pandas.csv", header=0)

# writing DataFrame to CSV file

data.to_csv("./data/test_data.csv", header=True, index=False, sep="|")
