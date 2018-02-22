import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
import numpy as np
style.use('ggplot')
rcParams.update({'font.size': 20})

fig, axes = plt.subplots(nrows=8, ncols=1, sharex=True, figsize=(30, 30))

df7 = pd.read_csv('Algonquin_Citygate.csv')
a = df7.plot(x='Trade date', y='Price', kind="line", color='b',subplots=False ,ax=axes[7],legend=False,title='Algonquin Citygates')
for line in axes[7].lines:
    line.set_linewidth(1)

df0 = pd.read_csv('TETCO_M3.csv')
g = df0.plot(x='Trade date', y='Price', kind="line", color='b',subplots=False, ax=axes[6],legend=False,title='TETCO-M3')

for line in axes[6].lines:
    line.set_linewidth(1)

df1 = pd.read_csv('Chicago_Citygates.csv')
b = df1.plot(x='Trade date', y='Price', kind="line", color='b',subplots=False, ax=axes[5],legend=False,title='Chicago Citygates')
for line in axes[5].lines:
    line.set_linewidth(1)

df2 = pd.read_csv('Henry.csv')
c = df2.plot(x='Trade date', y='Price', kind="line",\
 color='b',subplots=False, ax=axes[0],legend=False,title='Henry')
for line in axes[0].lines:
    line.set_linewidth(1)

df3 = pd.read_csv('Malin.csv')
df3.plot(x='Trade date', y='Price', kind="line"\
, color='b',subplots=False, ax=axes[1],legend=False,title='Malin')
for line in axes[1].lines:
    line.set_linewidth(1)

df4 = pd.read_csv('PG&E.csv')
e = df4.plot(x='Trade date', y='Price', kind="line", color='b',subplots=False, ax=axes[2],legend=False,title='PG&E-Citygate')
for line in axes[2].lines:
    line.set_linewidth(1)

df5 = pd.read_csv('Socal_Citygate.csv')
f = df5.plot(x='Trade date', y='Price', kind="line", color='b',subplots=False, ax=axes[4],legend=False,title='Socal-Citygate')
for line in axes[4].lines:
    line.set_linewidth(1)


df6 = pd.read_csv('Socal_Ehrenberg.csv')
i = df6.plot(x='Trade date', y='Price', kind="line", color='b',subplots=False, ax=axes[3],legend=False,title='Socal-Ehrenberg')
for line in axes[3].lines:
    line.set_linewidth(1)

axes[0].title.set_size(20)
axes[1].title.set_size(20)
axes[2].title.set_size(20)
axes[3].title.set_size(20)
axes[4].title.set_size(20)
axes[5].title.set_size(20)
axes[6].title.set_size(20)
axes[7].title.set_size(20)

plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.legend(bbox_to_anchor=(1.068, 5.2),loc='best')
plt.tick_params(axis='x', labelsize=22)

plt.xlabel("Date", color='black', fontsize='large')
plt.ylabel("U.S. Dollars per Million British Thermal Unit ($/MMBtu)",color='black',verticalalignment='center',horizontalalignment='center', position=(1,5.5))

plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
