import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

city = 'KS'
colors = ['red', 'blue', 'pink', 'brown', 'black', 'purple', 'yellow', 'grey', 'orange', 'magenta', 'green', 'beige']

plt.title("Kansas")
plt.xlabel("Beginning time")
plt.ylabel("Number")



for i in range(12):
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    df = pd.read_csv('Output\\spread_begin_' + str(i + 1) + '_' + city + '.csv')
    arr = df['number'].values
    plt.plot(x[(i + 1):], arr[:(12 - i)], color = colors[i])
    plt.plot(x[:i], arr[(12 - i):], color = colors[i])

plt.show()