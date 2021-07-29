import pandas as pd
import numpy as np

# a = {"bora" : "mat271e", 
# 	 "neco" : "fiz102e", 
# 	 "melih" : "eko201e", 
# 	 "fatih" : "blg252e"}
# aps = pd.Series(a)
# print(aps)
# print(aps.iloc[3])
# print(aps.loc['melih'])
# print(aps[3])
# print(aps['melih'])

# grades = pd.Series([50,60,70,80])

# total = 0
# for grade in grades:
#     total+=grade
# print(total/len(grades))

# total = np.sum(grades)
# print(total/len(grades))

# numbers = pd.Series(np.random.randint(0,1000,10000))
# print(numbers)

# print(numbers.head())
# print(len(numbers))

# numbers+=2
# print(numbers.head())

# s = pd.Series([1, 2, 3])
# s.loc['History'] = 102
# print(s)

a = {"bora" : "mat271e", 
	 "neco" : "fiz102e", 
	 "melih" : "eko201e", 
	 "fatih" : "blg252e"}
aps = pd.Series(a)

b = pd.Series(['mat122','mat123','mat124'], index=['Beyza','Beyza','Beyza'])

c = aps.append(b)
print(c)

