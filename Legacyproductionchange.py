import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 8
fig_size[1] = 4.6
df = pd.read_csv('Legacyproductionchange.csv')
df.dropna()
# df = df.iloc[::-1]
mycolors = ['g', 'orange', 'r', 'gray', 'c', 'limegreen', 'b']
a = df.plot(x = 'Month', y=['Appalachia', 'Haynesville', 'Eagle Ford', 'Anadarko', 'Permian', 'Niobrara', 'Bakken'], kind="area",stacked=False,alpha=0.4, color=mycolors)

for line in a.lines:
    line.set_linewidth(0)
a.xaxis.grid(False)
handles, labels = a.get_legend_handles_labels()
a.legend(handles[::-1], labels[::-1],bbox_to_anchor=(0.9, -0.13), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Million Cubic Feet per Day (MMcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()