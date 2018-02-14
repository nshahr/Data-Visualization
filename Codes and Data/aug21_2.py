import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
import numpy as np
from os import path
import pandas as pd
style.use('ggplot')
df = pd.read_csv('aug21_2.csv')
rcParams.update({'font.size': 12})
mycolors = ['#800080','gold']
a = df.plot(x = 'Month', y=['Total Natural Gas Consumption', 'Natural Gas Production Plus Net Imports'], kind="line",color=mycolors, xlim=(0,180),rot=40,fontsize=8, ylim=[0,120])

for line in a.lines:
    line.set_linewidth(2)

plt.ylabel('Billion Cubic Feet per Day (Bcf/d)',color='k')
plt.xlabel('Date',color='k')
a.legend(bbox_to_anchor=(1, 0.6), loc='best', ncol=1)
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
