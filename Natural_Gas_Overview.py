import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8.5
fig_size[1] = 4.7
df = pd.read_csv('Natural_Gas_Overview.csv')
df.dropna()
mycolors = ['r', 'b', 'g', 'saddlebrown']
a = df.plot(x = 'Month', y=['Production (Dry)', 'Consumption', 'Imports', 'Exports'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(1)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1.07, -0.13), loc='best', ncol=4, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet (Bcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()