import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('output\\spread_coordinate_DC.csv')
plt.scatter(df['x'], df['y'], color='blue', marker='o')

plt.title("Kansas")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

input()