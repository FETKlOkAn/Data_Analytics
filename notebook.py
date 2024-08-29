#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt
import pandas as pd

# Load dataset
grammys_data = pd.read_csv('solti_beyonce_grammys.csv')

# Set display options
plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

# Plot the data
fig = plt.figure(figsize=(15, 6))
fig.subplots_adjust(hspace=0.7)
plt.suptitle('Beyonce vs Solti', fontsize=30)

# Solti's plot
plt.subplot(2, 1, 1)
plt.bar(grammys_data.year, grammys_data.solti_nominated, color='cornflowerblue', label='Solti Nominated')
plt.bar(grammys_data.year, grammys_data.solti_won, bottom=grammys_data.solti_nominated, color='orange', label='Solti Won')
plt.title('Solti')
plt.ylim(0, 11)
plt.xlim(1961, 2025)
plt.legend(frameon=False)
plt.axvline(1999.5, linestyle='dashed')
plt.annotate('Solti: 31 wins, 74 nominations, from 1963 to 1999',
             xy=(1970, 9), fontsize=12, color='black', backgroundcolor='white',
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white'))

# Beyoncé's plot
plt.subplot(2, 1, 2)
plt.bar(grammys_data.year, grammys_data.beyonce_nominated, color='royalblue', label='Beyoncé Nominated')
plt.bar(grammys_data.year, grammys_data.beyonce_won, bottom=grammys_data.beyonce_nominated, color='pink', label='Beyoncé Won')
plt.title('Beyoncé')
plt.ylim(0, 11)
plt.xlim(1961, 2025)
plt.legend(frameon=False)
plt.axvline(1999.5, linestyle='dashed')
plt.annotate('Beyoncé: 32 wins, 88 nominations, from 2000 to today',
             xy=(1970, 5), fontsize=12, color='black', backgroundcolor='white',
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white'))

# Save the final chart
plt.savefig('Beyonce_vs_Solti.png', dpi=250)
plt.show()
