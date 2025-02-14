import pandas as pd
import numpy as np

df = pd.read_csv("auto-mpg.csv")
df[df.horsepower.str.isdigit()]
df = df.loc[df.horsepower.str.isdigit(), :]
df.horsepower = df.horsepower.astype(int)

origins = {1 : "USA", 2 : "Germany", 3 : "Japan"}
df.replace({"origin" : origins}, inplace=True)

# print(df.head())