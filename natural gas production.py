import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 10})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 6
df = pd.read_csv('Natural gas Production.csv')
df = df.iloc[::-1]
print(df.columns)
mycolor = ['#bf9b30', 'g', 'coral', '#4b3832', 'b', 'darkred', 'black']
a = df.plot(x = 'Month', y=[\
                            'Natural Gas Gross Withdrawals',\
                            'Dry Natural Gas Production',\
                            'Natural Gas Gross Withdrawals from Gas Wells',\
                            'Natural Gas Gross Withdrawals from Oil Wells',\
                            'Natural Gas Gross Withdrawals from Shale Gas',\
                            'Natural Gas Gross Withdrawals from Coalbed Wells',\
                            'Natural Gas Vented and Flared'\
                            ], kind="line", color=mycolor, ylim=(0,100))

for line in a.lines:
    line.set_linewidth(1.3)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1.02, -0.13), loc='best', ncol=2, fontsize='large')
plt.tick_params(axis='x', labelsize=9)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet per Day (Bcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()