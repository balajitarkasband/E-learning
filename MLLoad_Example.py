import pandas as pd
url = 'D:/python3.12/Scripts/courses.xlsx'
dataframe = pd.read_excel(url,header=0)
print(dataframe.head(2))