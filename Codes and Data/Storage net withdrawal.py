import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 4.2
plt.rcParams["figure.figsize"] = fig_size

df = pd.read_csv('Storage net withdrawals.csv')
df.dropna()
df = df.iloc[::-1]
mycolors = ['g', 'orange', 'b']
a = df.plot(x = 'Date', y=['Injections',\
                            'Withdrawals',\
                            'Net Withdrawals'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(0.7)
a.legend(bbox_to_anchor=(1, 0.7), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet per Day (Bcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
