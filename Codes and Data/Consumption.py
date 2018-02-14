import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('Consumption.csv')
df = df.iloc[::-1]
mycolors = ['#003366', '#20b2aa', '#ffc425', '#4f5b66', '#c0c5ce']
a = df.plot(x = 'Month', y=['Electric Power', 'Industrial', 'Residential', 'Commercial', 'Vehicle Fuel'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(2)
a.legend(bbox_to_anchor=(1, 0.7), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet per Day (Bcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()