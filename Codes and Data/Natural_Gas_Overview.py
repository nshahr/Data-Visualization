import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 10})

df = pd.read_csv('Natural_Gas_Overview.csv')
df.dropna()
mycolors = ['r', 'royalblue', 'blueviolet', 'grey']
a = df.plot(x = 'Month', y=['Production (Dry)', 'Consumption', 'Imports', 'Exports'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(2)
a.legend(bbox_to_anchor=(1, 0.7), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet (Bcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()