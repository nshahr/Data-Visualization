import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8.8
fig_size[1] = 4.8
df = pd.read_csv('storage.csv')
df = df.iloc[::-1]
df.dropna(inplace=True)
mycolors = ['c', 'saddlebrown', 'indigo', 'grey', 'g', 'orange', 'b']
a = df.plot(x = 'Month', y=['Capacity', 'Volume', 'Base Gas', 'Working Gas', 'Injections into Underground', 'Withdrawals', 'Net Withdrawals'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(1)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1.04, -0.12), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Million Cubic Feet (MMcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()