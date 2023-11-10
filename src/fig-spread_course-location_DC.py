import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

locs = ['FL', 'HI', 'AK', 'CA', 'KS']
start_months = [5, 9, 9, 8, 8]
loc = 'DC'
start_month = 9
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

df = pd.read_csv('Output\\spread_coordinate_' + loc + '.csv')
arrX = df['x'].to_numpy()
arrY = df['y'].to_numpy()
stat = df['status'].to_numpy()

max_distance = 30
mask = arrX < max_distance
arrX = arrX[mask]
arrY = arrY[mask]
stat = stat[mask]
mask = arrY < max_distance
arrX = arrX[mask]
arrY = arrY[mask]
stat = stat[mask]
mask = arrY > - max_distance
arrX = arrX[mask]
arrY = arrY[mask]
stat = stat[mask]

colors = []
for k in range(len(stat)):
    colors.append(stat_color[stat[k]])

plt.figure(figsize=(4, 8))
plt.scatter(arrX, arrY, s=0.5, c=colors, alpha=0.9)
xMax = axMax[loc]
plt.xlim([0, xMax])
plt.ylim([-xMax, xMax])
plt.yticks(range(-xMax, xMax + 1, 5))
plt.xticks(range(0, xMax + 1, 5))
plt.text(0.95 * xMax, -0.95 * xMax, loc, ha='right', va='bottom')
plt.tick_params(axis='y', which='both', left=True, right=False, labelleft=True, labelright=False)
plt.tick_params(axis='x', which='both', top=False, bottom=True, labeltop=False, labelbottom=True)

'''
gr = plt.Line2D([], [], color='#33AA55', marker='o', linestyle='None', markersize=2)
rd = plt.Line2D([], [], color='#FF0000', marker='o', linestyle='None', markersize=2)
be = plt.Line2D([], [], color='#0000FF', marker='o', linestyle='None', markersize=2)
bk = plt.Line2D([], [], color='#000000', marker='o', linestyle='None', markersize=2)
blank = plt.Line2D([], [])
plt.legend(handles=[be, gr, rd, bk], labels=['Seed', 'Developing / inter-dispersal', 'Dispersal', 'Dormancy / hold'], loc='upper center', ncol=4, bbox_to_anchor=(0.5,0.055))
'''
plt.text(33, -32.07, '(m)', ha='right', va='bottom')

plt.savefig('..\\figures\\spread_course-location_DC.pdf', bbox_inches = 'tight')
plt.show()