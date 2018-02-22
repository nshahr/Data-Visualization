import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8.8
fig_size[1] = 4.7
df = pd.read_csv('OH_PA_WV.csv')
df.dropna()
df = df.iloc[::-1]
mycolors = ['r', 'b', 'darkviolet', 'grey']
a = df.plot(x = 'Month', y=['Shale Gas', 'Gas Wells', 'Oil Wells', 'Coalbed Wells'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(1.5)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1.03, -0.12), loc='best', ncol=4, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet (Bcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()