import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 7.2
fig_size[1] = 4.8
df = pd.read_csv('production_per_rig.csv')
df.dropna()
# df = df.iloc[::-1]
mycolors = ['g', 'orange', 'r', 'gray', 'c', 'limegreen', 'b']
a = df.plot(x = 'Month', y=['Appalachia', 'Haynesville', 'Eagle Ford', 'Niobrara', 'Anadarko', 'Bakken', 'Permian'], kind="area",stacked=False,alpha=0.78 ,color=mycolors)

for line in a.lines:
    line.set_linewidth(0)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(0.96, -0.11), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Thousand Cubic Feet per Day (Mcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()