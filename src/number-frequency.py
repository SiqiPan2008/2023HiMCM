import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Output\\spread_result_FL.csv')

numArr = df['number'].to_numpy()
distArr = df['distance'].to_numpy()

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2))


ax1.hist(numArr, bins = 30, color = '#5588DD', edgecolor='black', alpha = 0.8, density = True)
ax2.hist(distArr, bins = 30, color = '#5588DD', edgecolor='black', alpha = 0.8, density = True)

ax1.set_xlabel('Number')
ax2.set_xlabel('Mean distance (m)')
ax1.set_ylabel('Frequency / bin width')
ax2.yaxis.tick_right()

plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\number-frequency.pdf', bbox_inches = 'tight')
#plt.show()