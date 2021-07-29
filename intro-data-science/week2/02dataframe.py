import pandas as pd

r1 = pd.Series({'Name': 'Bora', 'Class': 'fiz102e', 'Score': 75})
r2 = pd.Series({'Name': 'Melih', 'Class': 'eko201e', 'Score': 100})
r3 = pd.Series({'Name': 'Beyza', 'Class': 'skolastik', 'Score': 60})

df = pd.DataFrame([r1,r2,r3], index=['school1','school2','school1'])

print(df.head())