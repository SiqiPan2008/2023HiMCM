import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

df = pd.read_csv('Output\\spread_result_time_FL.csv')

mArr = df['month'].to_numpy()
numArr = df['number'].to_numpy()
distArr = df['mean_distance'].to_numpy()

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax2.plot(mArr, distArr, 'b-', label='y2')
ax1.plot(mArr, numArr, 'r-', label='y1')

ax1.set_xlabel('Time (month)')
ax1.set_ylabel('Number')
ax2.set_xlabel('Mean distance (m)')

plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\number-time.pdf', bbox_inches = 'tight')
plt.show()