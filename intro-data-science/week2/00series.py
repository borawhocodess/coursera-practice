import pandas as pd

a = ["bora", "neco", "fatih"]
aps = pd.Series(a)
print(aps)

a = [1, 2, 3]
aps = pd.Series(a)
print(aps)

a = ["bora", "neco", None]
aps = pd.Series(a)
print(aps)

a = [1, 2, None]
aps = pd.Series(a)
print(aps) # NaN

import numpy as np

print(np.nan == None, np.nan == np.nan, np.isnan(np.nan)) # WOW

a = {"bora" : "mat271e", 
	 "neco" : "fiz102e", 
	 "fatih" : "blg252e"}
aps = pd.Series(a)
print(aps)
print(aps.index)

aps = pd.Series(["mat271e", "fiz102e", "blg252e"], index=["bora", "neco", "fatih"])
print(aps)

b = ["bora", "fatih", "alp"]
aps = pd.Series(a, index=b)
print(aps)

