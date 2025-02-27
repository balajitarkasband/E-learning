import pandas as pd

urll = r'D:/python3.12/Scripts/Employee.json'
dataframe = pd.read_json(urll)
print(dataframe.head(2))
