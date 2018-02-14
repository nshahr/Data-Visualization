import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('Henry_Hub_Natural_Gas_Spot_Price.csv')
df = df.iloc[::-1]

a = df.plot(x = 'Date', y='Henry Hub Daily Price', kind="line", color='b', ms=10)

for line in a.lines:
    line.set_linewidth(0.7)
a.legend(bbox_to_anchor=(1, 0.7), loc='best', ncol=2)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("US Dollars per Million Cubic Feet ($/Mcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()