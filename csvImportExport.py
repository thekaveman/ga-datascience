import pandas as pd

# loading DataFrame from a CSV file

csvData = pd.read_csv("./data/test_pandas.csv", header=0)

# writing DataFrame to CSV file

csvData.to_csv("./data/test_data.csv", header=True, index=False, sep="|")
