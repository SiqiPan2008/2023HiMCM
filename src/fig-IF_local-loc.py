import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

x = np.arange(1, 16, 1)
plants = ['Sweetclover', 'Tree of heaven', 'Yellow salsify', 'Dandelion', 'Mugo pine']
nlabel = [2, 3, 2, 2, 2]
slabel = [0, 2, 5, 7, 9]
colors = ['#4444CC', '#888888', '#FFFFFF', 
          '#4444CC', '#CCCC44', '#888888', '#FFFFFF', 
          '#4444CC', '#888888', '#FFFFFF', 
          '#4444CC', '#CCCC44', '#FFFFFF', 
          '#4444CC', '#888888']
labels = ['FL', 'AK', '',
          'FL', 'NV', 'AK', '',
          'FL', 'AK', '',
          'FL', 'NV', '',
          'FL', 'AK']

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
xticks[2].set_visible(False)
xticks[6].set_visible(False)
xticks[9].set_visible(False)
xticks[12].set_visible(False)
h = 89
rot = 0
plt.text(1.5, h, plants[0], ha='center', rotation = rot)
plt.text(5, h, plants[1], ha='center', rotation = rot)
plt.text(8.5, h, plants[2], ha='center', rotation = rot)
plt.text(11.5, h, plants[3], ha='center', rotation = rot)
plt.text(14.5, h, plants[4], ha='center', rotation = rot)
plt.axvline(x=3, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=7, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=10, linestyle='--', color='grey', linewidth=0.3)
plt.axvline(x=13, linestyle='--', color='grey', linewidth=0.3)



plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\IF_local-loc.pdf', bbox_inches = 'tight')
plt.show()