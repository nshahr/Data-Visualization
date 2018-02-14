import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 10})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 9
fig_size[1] = 5

df = pd.read_csv('Consumption PA.csv')

a = df.plot(x = 'Date', y='Pensylvania Residential Naural Gas Consumption', kind="line", color='b', ms=10)

for line in a.lines:
    line.set_linewidth(0.7)
a.legend(bbox_to_anchor=(1, 0.55), loc='best', ncol=2)
plt.tick_params(axis='x', labelsize=9)
plt.xlabel("Date", color='black')
plt.ylabel("Million Cubic Feet per Day(MMcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()