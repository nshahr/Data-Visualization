import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size':9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 9
fig_size[1] = 4.2
df = pd.read_csv('export price.csv')
df.dropna()
df = df.iloc[::-1]
print(df.columns)
mycolors = ['r', 'g', 'orange', 'gray', 'c']
a = df.plot(x = 'Month', y=['U.S. LNG Exports',\
                            'U.S. Natural Gas Pipeline Exports to Canada',\
                            'U.S. Natural Gas Pipeline Exports to Mexico'], kind="line", color=mycolors)
for line in a.lines:
    line.set_linewidth(1)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(0.84, -0.14), loc='best', ncol=1, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("U.S. Dollars per Million British Thermal Unit ($/MMBtu)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
