import pandas as pd

sales = [100,130,119,92,35]
customer_account = ['B100','J101','X102','P103','R104']
city = ['SF','NYC','LA','CHI','BOS']

# create a DataFrame with the above data

df = pd.DataFrame({
    "sales": sales,
    "customer_account": customer_account,
    "city": city
})
