import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
import matplotlib
style.use('ggplot')
rcParams.update({'font.size': 9})
fig, ax1 = plt.subplots(sharex=True)
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 9.4
fig_size[1] = 4.6
df = pd.read_excel('Rig_Production.xlsx')
df.dropna()
# df = df.iloc[::-1]
a = df.plot(x = 'Date', y=['Dry Natural Gas Production'], kind="area", color='gold', ax=ax1)
for line in a.lines:
    line.set_linewidth(0.7)
ax2 = ax1.twinx()
b = df.plot(x = 'Date', y=['Weekly Rig Count'], kind="line", color='black', ax=ax2)

ax1.grid()
l = ax1.get_ylim()
l2 = ax2.get_ylim()
f = lambda x : l2[0]+(x-l[0])/(l[1]-l[0])*(l2[1]-l2[0])
ticks = f(ax1.get_yticks())
ax2.yaxis.set_major_locator(matplotlib.ticker.FixedLocator(ticks))
ax1.xaxis.grid(False)
ax2.xaxis.grid(False)
ax1.legend(bbox_to_anchor=(0.58, -0.17), loc='best', ncol=1, fontsize='x-large')
ax2.legend(bbox_to_anchor=(1.08, -0.17), loc='best', ncol=1, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
ax1.set_xlabel("Date", color='black')
ax1.set_ylabel("Billion Cubic feet per Day (Bcf/d)",color='black')
ax2.set_ylabel("Rig Count",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
