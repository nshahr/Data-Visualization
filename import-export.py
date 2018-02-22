import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 7
fig_size[1] = 4.7
print(fig_size)
df = pd.read_csv('import-export.csv')
df = df.iloc[::-1]
mycolor = ['g', 'saddlebrown', '#0392cf', 'gold']
a = df.plot(x = 'Month', y=['Imports', 'Exports', 'Liquefied Imports', 'Liquefied Exports'], kind="line", color=mycolor)

for line in a.lines:
    line.set_linewidth(1)
a.legend(bbox_to_anchor=(0.88, -0.12), loc='best', ncol=2, fontsize='x-large')
a.xaxis.grid(False)
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet per Day (Bcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()