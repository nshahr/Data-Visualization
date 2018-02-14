import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('production_per_rig.csv')
df.dropna()
# df = df.iloc[::-1]
mycolors = ['g', 'orange', 'r', 'gray', 'c', 'limegreen', 'b']
a = df.plot(x = 'Month', y=['Appalachia', 'Haynesville', 'Eagle Ford', 'Niobrara', 'Anadarko', 'Bakken', 'Permian'], kind="area",stacked=False,alpha=0.4 ,color=mycolors)

for line in a.lines:
    line.set_linewidth(2)
a.legend(bbox_to_anchor=(1, 0.7), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("Thousand Cubic Feet per Day (Mcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()