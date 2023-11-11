import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = []
for i in range(12):
    a = []
    data.append(a)
for i in range(12):
    df = pd.read_csv('Output\\spread_begin_' + str(i+1) + '_FL.csv')
    numArr = df['number'].
    for j in range(12):
        data[j].append()

plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\start_month-number.pdf', bbox_inches = 'tight')
plt.show()