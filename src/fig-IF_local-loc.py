import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

x = np.arange(1, 14, 1)
plants = ['Sweetclover', 'Tree of heaven', 'Yellow salsify', 'Dandelion']
nlabel = [3, 2, 2, 3]
slabel = [0, 3, 5, 7]
colors = ['#888888', '#4444CC', '#CCCC44', '#FFFFFF', 
          '#4444CC', '#CCCC44', '#FFFFFF', 
          '#888888', '#CCCC44', '#FFFFFF', 
          '#888888', '#4444CC', '#CCCC44']
labels = ['AK', 'FL', 'NV', '',
          'FL', 'NV', '',
          'AK', 'NV', '',
          'AK', 'FL', 'NV']

w = 0.4
plt.figure(figsize=(5, 2))

df = pd.read_csv('Input\\plant_local_analysis.csv')
imfac = df['Impact factor'].values
imfacB = []
for i in range(len(plants)):
    for j in range(nlabel[i]):
        imfacB.append(imfac[slabel[i] + j])
    if i != len(plants) - 1:
        imfacB.append(0)


plt.grid(axis='y', linewidth=0.3)
plt.bar(x, imfacB, color=colors, label=labels, width=w, edgecolor='black', alpha=0.8, linewidth = 0.3)

plt.ylim([14, 86])
plt.ylabel('Local impact factor')
plt.xticks(x, labels)
ax = plt.gca()
ax.set_axisbelow(True)
xticks = ax.xaxis.get_major_ticks()
xticks[3].set_visible(False)
xticks[6].set_visible(False)
xticks[9].set_visible(False)
h = 89
rot = 0
plt.text(2, h, plants[0], ha='center', rotation = rot)
plt.text(5.5, h, plants[1], ha='center', rotation = rot)
plt.text(8.5, h, plants[2], ha='center', rotation = rot)
plt.text(12, h, plants[3], ha='center', rotation = rot)
plt.axvline(x=4, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=7, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=10, linestyle='--', color='grey', linewidth=0.3)

plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\IF_local-loc.pdf', bbox_inches = 'tight')
plt.show()