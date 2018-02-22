import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
import matplotlib
from os import path
style.use('ggplot')
# rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8
fig_size[1] = 4.2
fig, ax1 = plt.subplots()
df = pd.read_excel('Henry_Rig_Price.xlsx')

b = df.plot(x = 'Date', y=['Weekly Rig Count'], kind="line", color='black', ax=ax1)
ax2 = ax1.twinx()
a = df.plot(x = 'Date', y=['Henry Hub Spot Price'], kind="line", color='b', ax=ax2)
ax1.grid()
l = ax1.get_ylim()
l2 = ax2.get_ylim()
f = lambda x : l2[0]+(x-l[0])/(l[1]-l[0])*(l2[1]-l2[0])
ticks = f(ax1.get_yticks())
ax2.yaxis.set_major_locator(matplotlib.ticker.FixedLocator(ticks))

ax1.legend(bbox_to_anchor=(0.45, -0.22), loc='best', ncol=1)
ax2.legend(bbox_to_anchor=(0.85, -0.22), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=8)
ax1.set_xlabel("Date", color='black')
ax1.set_ylabel("U.S. Dollars per Million British Thermal Unit ($/MMBtu)",color='black')
ax2.set_ylabel("Rig Count",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
