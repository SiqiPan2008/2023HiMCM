import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Output\\spread_result_FL.csv')

numArr = df['number'].to_numpy()
distArr = df['distance'].to_numpy()

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

fig, subplots = plt.subplots(2, 6, figsize=(9, 6))

rows = 2
cols = 6
for i in range(rows):
    for j in range(cols):
        df = pd.read_csv('Output\\spread_course_' + str(cols * i + j + 1) + '_FL' + '.csv')
        arrX = df['x'].values
        arrY = df['y'].values
        stat = df['status'].values
        colors = []
        for k in range(len(stat)):
            colors.append(stat_color[stat[k]])

        subplots[i, j].scatter(arrX, arrY, s=0.5, c=colors, alpha=0.9)
        subplots[i, j].set_xlim([0, 10])
        subplots[i, j].set_ylim([-10, 10])
        subplots[i, j].set_yticks([-10, -5, 0, 5, 10])
        subplots[i, j].set_xticks([0, 5, 10])
        subplots[i, j].text(9.5, -9.5, months[(cols * i + j + 4) % 12] + ' 1st', ha='right', va='bottom')
        if i != rows - 1:
            subplots[i, j].tick_params(axis='x', which='both', top=False, bottom=False, labeltop=False, labelbottom=False)
        if j != 0:
            subplots[i, j].tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False)

gr = plt.Line2D([], [], color='#33AA55', marker='o', linestyle='None', markersize=2)
rd = plt.Line2D([], [], color='#FF0000', marker='o', linestyle='None', markersize=2)
be = plt.Line2D([], [], color='#0000FF', marker='o', linestyle='None', markersize=2)
bk = plt.Line2D([], [], color='#000000', marker='o', linestyle='None', markersize=2)
blank = plt.Line2D([], [])
fig.legend(handles=[be, gr, rd, bk], labels=['Seed', 'Developing / inter-dispersal', 'Dispersal', 'Dormancy / hold'], loc='lower center', ncol=4, bbox_to_anchor=(0.5,0.03))
fig.text(0.926, 0.08, '(m)', ha='right', va='bottom')

plt.subplots_adjust(wspace=0.1, hspace=0.05)
plt.savefig('..\\figures\\spread_course-time.pdf', bbox_inches = 'tight')
plt.show()