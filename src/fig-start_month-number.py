import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

x = np.arange(1, 13, 1)
colors = [
    '#559999',
    '#995599',
    '#999955',

    '#444444',

    '#00CCCC',
    '#CC00CC',
    '#CCCC00',

    '#888888',

    '#EE0000',
    '#00EE00',
    '#0000EE',

    '#CCCCCC'
    
]
months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
devm = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
w = 0.6

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 2))



increment = []
cumulative = []
for i in range(12):
    a = []
    b = []
    increment.append(a)
    cumulative.append(b)
for i in range(12):
    df = pd.read_csv('Output\\spread_begin_' + str(i+1) + '_FL.csv')
    arr = df['number'].values
    increment[0].append(arr[0])
    cumulative[0].append(arr[0])
    for j in range(11):
        increment[j + 1].append(arr[j + 1] - arr[j])
        cumulative[j + 1].append(arr[j + 1])

ax1.bar(x, increment[0], color=colors[0], label = devm[0], width=w)
for i in range(11):
    ax1.bar(x, increment[i + 1], color=colors[i + 1], bottom = cumulative[i], label = devm[i + 1], width=w)



increment = []
cumulative = []
for i in range(12):
    a = []
    b = []
    increment.append(a)
    cumulative.append(b)
for i in range(12):
    df = pd.read_csv('Output\\spread_begin_' + str(i+1) + '_FL.csv')
    arr = df['mean_distance'].values
    increment[0].append(arr[0])
    cumulative[0].append(arr[0])
    for j in range(11):
        increment[j + 1].append(arr[j + 1] - arr[j])
        cumulative[j + 1].append(arr[j + 1])

ax2.bar(x, increment[0], color=colors[0], label = devm[0], width=w)
for i in range(11):
    ax2.bar(x, increment[i + 1], color=colors[i + 1], bottom = cumulative[i], label = devm[i + 1], width=w)


handles, labels = plt.gca().get_legend_handles_labels()
order = [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11]
ax2.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper right', bbox_to_anchor = (0.645, -0.22), ncols=6)
ax1.set_ylabel('Number')
ax2.set_ylabel('Mean distance (m)', rotation = -90, labelpad = 10)
ax1.set_xlabel('Starting month')
ax2.set_xlabel('Starting month')
ax1.set_xticks(x, months)
ax2.set_xticks(x, months)
ax1.set_ylim([0, 1000])
ax2.set_ylim([0, 6])
ax2.yaxis.set_label_position('right')
ax2.yaxis.tick_right()



plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\start_month-number.pdf', bbox_inches = 'tight')
plt.show()