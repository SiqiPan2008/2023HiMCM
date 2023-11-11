import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

x = np.arange(1, 23, 1)
cat = ['Growth Rate', 'Fruit Seed Abundance', 'Seed Spread Rate', 'Seedling Vigor', 'Toxicity']
ncat = [3, 4, 4, 3, 4]
scat = [0, 4, 9, 14, 18]
colors = ['#00CC00', '#00CC00', '#00CC00', '#FFFFFF', 
        '#CC8844', '#CC8844', '#CC8844', '#CC8844', '#FFFFFF', 
        '#0000CC', '#0000CC', '#0000CC', '#0000CC', '#FFFFFF', 
        '#CC0000', '#CC0000', '#CC0000', '#FFFFFF', 
        '#990099', '#990099', '#990099', '#990099']
labels = ['Slow', 'Moderate', 'Rapid', '',
          'None', 'Low', 'Medium', 'High', '',
          'None', 'Slow', 'Moderate', 'Rapid', '',
          'Low', 'Medium', 'High', '',
          'None', 'Slight', 'Moderate', 'Severe']
lpos = [2, 0, 1, 0,
        3, 1, 2, 0, 0,
        1, 3, 0, 2, 0,
        1, 2, 0, 0,
        1, 3, 0, 2]
w = 0.4
plt.figure(figsize=(6, 2))

mins = []
ranges = []
for i in range(len(cat)):
    df = pd.read_csv('Output\\IF\\' + cat[i] + '.csv')
    rowlabel = df['Row Labels'].to_numpy()
    min = df['Min of Impact factor'].to_numpy()
    max = df['Max of Impact factor2'].to_numpy()
    for j in range(ncat[i]):
        label = labels[scat[i] + j]
        index = lpos[scat[i] + j]
        mins.append(min[index])
        ranges.append(max[index] - min[index])
    if i != len(cat) - 1:
        mins.append(0)
        ranges.append(0)

plt.grid(axis='y', linewidth=0.3)
plt.bar(x, mins, color='white', label=labels, width=w, alpha=0)
plt.bar(x, ranges, color=colors, label=labels, width=w, edgecolor='black', bottom = mins, alpha=0.7, linewidth = 0.3)
plt.ylim([30, 90])
plt.ylabel('Global impact factor')
plt.xticks(x, labels, rotation = -90)
ax = plt.gca()
ax.set_axisbelow(True)
xticks = ax.xaxis.get_major_ticks()
xticks[3].set_visible(False)
xticks[8].set_visible(False)
xticks[13].set_visible(False)
xticks[17].set_visible(False)
h = 92.5
plt.text(2, h, 'Growth rate', ha='center')
plt.text(6.5, h, 'Fruit/seed abundance', ha='center')
plt.text(11.5, h, 'Seed spread rate', ha='center')
plt.text(16, h, 'Seedling vigor', ha='center')
plt.text(20.5, h, 'Toxicity', ha='center')
plt.axvline(x=4, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=9, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=14, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=18, linestyle='--', color='grey', linewidth=0.3)



plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\categories-IF.pdf', bbox_inches = 'tight')
plt.show()