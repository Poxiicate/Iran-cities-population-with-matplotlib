import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("city.csv")

sizes = (df["population"]) / 4000

x = range(len(df))

plt.scatter(df["city name"], df["population"], s=sizes)
plt.title("Population of Iranian Cities")
plt.xlabel("city Name")
plt.ylabel("Population")
plt.grid()
plt.show()