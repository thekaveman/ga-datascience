import pandas as pd

# loading DataFrame from an Excel file

excelData = pd.read_excel("./data/test_pandas.xlsm", "Sheet1")

# writing DataFrame to an Excel file

writer = pd.ExcelWriter("./data/test_sheets.xlsx")
data.to_excel(writer, "Original")
data.to_excel(writer, "Copy")
writer.save()
