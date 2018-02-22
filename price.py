import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 9
fig_size[1] = 4.2

df = pd.read_csv('price.csv')
df.dropna()
df = df.iloc[::-1]
mycolors = ['g', 'orange', 'r', 'gray', 'c']
a = df.plot(x = 'Month', y=['Residential', 'Commercial Consumers', 'Industrial', 'Electric Power', 'Wellhead'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(1.3)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1, -0.12), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("U.S. Dollars per Million British Thermal Unit ($/MMBtu)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
