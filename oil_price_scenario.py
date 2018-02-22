import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig, ax = plt.subplots(figsize=(11,5), sharey=True)
# fig_size = plt.rcParams["figure.figsize"]
# fig_size[0] = 10
# fig_size[1] = 5

mycolor = ['g', 'saddlebrown', 'b', 'black']
dff = pd.read_csv('Oil_Spot_Prices.csv')
a = dff.plot(x = 'Date', y=['High Oil Price', 'Base Oil Price', 'Low Oil Price','Cushing OK WTI Spot Price'], kind="line", color=mycolor, ax=ax)

for line in a.lines:
    line.set_linewidth(1.2)
a.xaxis.grid(False)
plt.axvline(x=335, ymin=0, ymax=0.85, dash_capstyle='butt', color='black', dash_joinstyle='miter', ls='--')

a.legend(bbox_to_anchor=(1.05, -0.11), loc='best', ncol=4, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Dollars per Barrel ($/bbl)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()