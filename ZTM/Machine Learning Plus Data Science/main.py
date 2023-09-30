# 1 - import the data
# 2 - clean the data
# 3 - split the data into training set and testing set
# 4 - create the model
# 5 - check the output

import pandas as pd

df = pd.read_csv("data.csv")

print(df.describe())

print(df.values)


for item in df.values:
    print(item[0], item[2])


def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    
    if "K" in x:
        if len(x) > 1:
            return float(x.replace("K", "")) * 1000
        return 1000.0
    
    if "M" in x:
        if len(x) > 1:
            return float(x.replace("M", "")) * 1000000
        return 1000000.0
    
    if "B" in x:
        if len(x) > 1:
            return float(x.replace("B", "")) * 1000000000
    return 0.0
