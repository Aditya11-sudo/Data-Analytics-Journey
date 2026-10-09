import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())

df = pd.read_csv(r"data/students.csv")
# print(df.head())

# print(df[["Python","SQL","c++","Statistics","Machine Learning"]].sum(axis=1))
#axis=1 means sum across the rows, axis=0 means sum across the columns
df["Total"]=df[["Python","SQL","C++","statistics","Machine Learning"]].sum(axis=1)
# print(df.head(10))
df["Percentage"]=(df["Total"]/5).round(1)
# print(df.head(5))

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else :
        return "F"

   
df["Grade"]=df["Percentage"].apply(calculate_grade)
# print(df.head(5))

# print(df["Percentage"]>90)
# here iam using single,multiple conditions to filter multiple columns in dataframe
high_scorers=df[df["Percentage"]>90]
# high_scorers=df[(df["Percentage"]>90)& (df["Grade"]=="A+")] #here we use and condition
# high_scorers=df[(df["Percentage"]>90) | (df["Grade"]=="A+")] #here we used or condition 
# print(high_scorers)
df = df.sort_values(by="Percentage", ascending=False)
print(df)