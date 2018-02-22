import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig, axes = plt.subplots(sharex=True, sharey=True, figsize=(18, 6))

df = pd.read_csv('EIA Reference case - with power plan.csv')
df.dropna()
df = df.iloc[::-1]
print(df.columns)
mycolors = ['#6b3d4b', 'c', 'g', 'r', '#4b3832']

a = df.plot(x = 'Year', y=[
    'Coal',
    'Natural Gas',
    'Renewable Sources',
    'Nuclear',
    'Petroleum'
], kind="line", color=mycolors, ylim=[0,2000], ax=axes, legend=True)
for line in a.lines:
    line.set_linewidth(1)

dff = pd.read_csv('EIA Reference without power plan.csv')
dff = dff.iloc[::-1]
b = dff.plot(x = 'Year', y=[
    'Coal',
    'Natural Gas',
    'Renewable Sources',
    'Nuclear',
    'Petroleum'
], kind="line", style='--', color=mycolors, ylim=[0,2000], ax=axes)

for line in b.lines:
    line.set_linewidth(1)

axes.text(2040.5, 1820, "Refrence Case", horizontalalignment='left', fontsize=12)
axes.text(2040.5, 1660, "Without Clean Power Plan", horizontalalignment='left', fontsize=12)
axes.xaxis.grid(False)
axes.tick_params(axis='x', labelsize=8)
axes.set_xlabel("Date", color='black')
axes.legend(bbox_to_anchor=(1.2, -.12),loc='best', ncol=10, fontsize='x-large')
axes.set_ylabel("Billion Kilowatt Hours (Bkwh)",color='black')
# plt.tight_layout(pad=5, w_pad=1, h_pad=1.44)
axes.axvline(x=0.8, ymin=0, ymax=1, dash_capstyle='butt', color='black', dash_joinstyle='miter', ls='--')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')

# plt.show()
