import pandas as pd
import sqlite3

# establish a connection to the sqlite db
conn = sqlite3.connect("./data/test_pandas.db")

# query the database and load into DataFrame

query = "SELECT * FROM test"
data = pd.read_sql(query, conn)
