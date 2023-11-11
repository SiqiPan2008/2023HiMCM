import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Output\\IF\\IF_Frequency.csv')

imfac = df['Impact factor'].to_numpy()

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

plt.figure(figsize = (4, 2))

plt.hist(imfac, bins = 30, color = '#5588DD', edgecolor='black', alpha = 0.8, density = True, linewidth = 0.3)

plt.xlabel('Impact factor')
plt.ylabel('Frequency / bin width')

plt.subplots_adjust(wspace=0.04, hspace=0)
plt.savefig('..\\figures\\IF-frequency.pdf', bbox_inches = 'tight')
plt.show()