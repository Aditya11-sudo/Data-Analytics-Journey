import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())

df = pd.read_csv(r"data\students.csv")
# print(df.head())

# print(df[["Python","SQL","c++","Statistics","Machine Learning"]].sum(axis=1))
#axis=1 means sum across the rows, axis=0 means sum across the columns
df["Total"]=df[["Python","SQL","C++","statistics","Machine Learning"]].sum(axis=1)
print(df.head(5))
df["Percentage"]=df["Total"]/5
print(df.head(5))
