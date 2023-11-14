import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['cmr10']
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['font.size'] = 7.5

params = ['MuT', 'StdT', 'MuW', 'StdW', 'Hum']
param_data = [
    (r'$\mu_T$ ($^\circ$C)', 300, 100),
    (r'$\sigma_T$ ($^\circ$C)', 100, 50),
    (r'$\mu_W$ (m/s)', 150, 50),
    (r'$\sigma_W$ (m/s)', 100, 50),
    (r'$\mu_H$ (%)', 1000, 500)
]

for p in range(5):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(3, 1.5))

    df = pd.read_csv('Output\\' + params[p] + '_sa.csv')
    pVal = df[params[p]].to_numpy()
    if p == 4:
        pVal *= 100
    num = df['number'].to_numpy()
    dist = df['mean_distance'].to_numpy()

    ax1.plot(pVal, num, color='#4477AA', linewidth = 0.6)
    ax2.plot(pVal, dist, color='#4477AA', linewidth = 0.6)

    ax1.set_xlabel(param_data[p][0])
    ax2.set_xlabel(param_data[p][0])
    ax1.set_ylabel('Number')
    ax2.set_ylabel('Mean distance (m)', rotation = -90, labelpad = 12)

    ax1.set_xticks(np.arange(0, param_data[p][1] + 1, param_data[p][2]) / 10)
    ax2.set_xticks(np.arange(0, param_data[p][1] + 1, param_data[p][2]) / 10)
    ax2.yaxis.set_label_position('right')
    ax2.tick_params(axis='y', which='both', left=False, right=True, labelleft=False, labelright=True)

    plt.subplots_adjust(wspace=0.04, hspace=0)
    plt.savefig('..\\figures\\sa_' + params[p] + '.pdf', bbox_inches = 'tight')
    #plt.show()