import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

x = np.linspace(0, 4, 1000)
y = -0.25 * np.cos(np.pi / 2 * x) + 0.1

plt.plot(x, y)

plt.savefig('..\\figures\\cosine.pdf', bbox_inches = 'tight')
plt.show()