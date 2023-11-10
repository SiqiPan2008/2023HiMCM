import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

locs = ['AK', 'CA', 'HI', 'FL', 'KS', 'DC']
colors = ['#555555', '#EE8800', '#BBBB00', '#0000FF', '#227722', '#FF0000']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 2.5))

ax1.set_xticks(range(0,365,30))
ax2.set_xticks(range(0,365,30))
ax2.tick_params(axis='y', which='both', left=False, right=True, labelleft=False, labelright=True)
hd = []
for i in range(6):
    df = pd.read_csv('Output\\spread_day_result_' + locs[i] + '.csv')
    x = df['day'].to_numpy()
    num = df['number'].to_numpy()
    ln_num = np.log(num)
    dist = df['mean_distance'].to_numpy()

    ax1.plot(x, ln_num, c = colors[i], linewidth = 0.6)
    ax2.plot(x, dist, c = colors[i], linewidth = 0.6)

ax1.set_xlabel('Time (day)')
ax2.set_xlabel('Time (day)')
ax1.set_ylabel('ln(number)')
ax2.set_ylabel('Mean distance (m)', rotation = -90, labelpad = 10)
ax2.yaxis.set_label_position('right')

for i in range(6):
    hd.append(plt.Line2D([], [], color = colors[i]))
ax2.legend(handles=hd, labels=locs, loc='upper right', ncol=6, bbox_to_anchor=(0.65,-0.2))

plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\number_mean_distance-time.pdf', bbox_inches = 'tight')
plt.show()