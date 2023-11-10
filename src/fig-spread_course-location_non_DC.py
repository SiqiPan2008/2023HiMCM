import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Output\\spread_result_FL.csv')

numArr = df['number'].to_numpy()
distArr = df['distance'].to_numpy()

locs = ['AK', 'CA', 'HI', 'FL', 'KS']
axMax = {
    'FL': 10,
    'HI': 10,
    'AK': 10,
    'DC': 30,
    'KS': 10,
    'CA': 10
}


stat_color = {
    'Status.Dev': '#33AA55', 
    'Status.InterDis': '#33AA55', 
    'Status.Dis': '#FF0000', 
    'Status.Seed': '#0000FF',
    'Status.Hold': '#000000',
    'Status.Dormancy': '#000000'
}

months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['cmr10'],
    'axes.unicode_minus': False,
    'font.size': 7.5
})

cols = 5
fig, subplots = plt.subplots(1, cols, figsize=(8, 16/5))

for i in range(cols):
    df = pd.read_csv('Output\\spread_coordinate_' + locs[i] + '.csv')
    arrX = df['x'].values
    arrY = df['y'].values
    stat = df['status'].values
    colors = []
    for k in range(len(stat)):
        colors.append(stat_color[stat[k]])

    subplots[i].scatter(arrX, arrY, s=0.5, c=colors, alpha=0.9)
    xMax = axMax[locs[i]]
    subplots[i].set_xlim([0, xMax])
    subplots[i].set_ylim([-xMax, xMax])
    subplots[i].set_yticks([-xMax, -xMax / 2, 0, xMax / 2, xMax])
    subplots[i].set_xticks([0, xMax / 2, xMax])
    subplots[i].text(0.95 * xMax, -0.95 * xMax, locs[i], ha='right', va='bottom')
    if i != 0:
        subplots[i].tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False)
    subplots[i].tick_params(axis='x', which='both', top=False, bottom=True, labeltop=False, labelbottom=True)

gr = plt.Line2D([], [], color='#33AA55', marker='o', linestyle='None', markersize=2)
rd = plt.Line2D([], [], color='#FF0000', marker='o', linestyle='None', markersize=2)
be = plt.Line2D([], [], color='#0000FF', marker='o', linestyle='None', markersize=2)
bk = plt.Line2D([], [], color='#000000', marker='o', linestyle='None', markersize=2)
blank = plt.Line2D([], [])
fig.legend(handles=[be, gr, rd, bk], labels=['Seed', 'Developing / inter-dispersal', 'Dispersal', 'Dormancy / hold'], loc='upper center', ncol=4, bbox_to_anchor=(0.5,0.055))
fig.text(0.929, 0.053, '(m)', ha='right', va='bottom')

plt.subplots_adjust(wspace=0.1, hspace=0.05)
plt.savefig('..\\figures\\spread_course-location_non_DC.pdf', bbox_inches = 'tight')
plt.show()