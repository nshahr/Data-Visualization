import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('export price.csv')
df.dropna()
df = df.iloc[::-1]
print(df.columns)
mycolors = ['r', 'g', 'orange', 'gray', 'c']
a = df.plot(x = 'Month', y=['U.S. LNG Exports',\
                            'U.S. Natural Gas Pipeline Exports to Canada',\
                            'U.S. Natural Gas Pipeline Exports to Mexico'], kind="line", color=mycolors)
for line in a.lines:
    line.set_linewidth(2)
a.legend(bbox_to_anchor=(1, 0.65), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("US Dollars per Million Cubic Feet ($/MMcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
