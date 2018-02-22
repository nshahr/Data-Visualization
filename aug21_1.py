import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
import numpy as np
from os import path
import pandas as pd
style.use('ggplot')

df = pd.read_csv('aug21_1.csv')
df = df[::-1]
rcParams.update({'font.size': 9})
mycolors = ['#003366', '#20b2aa', '#ffc425', '#4f5b66', '#c0c5ce']
a = df.plot(x = 'Year', y=['Electric Power','Industrial', 'Residential', 'Commercial', 'Vehicle Fuel'][::-1], kind="bar", stacked=True,color=mycolors[::-1])

plt.ylabel('U.S. Gas Demand',color='k')
plt.ylabel('Trillion Cubic Feet (Tcf)',color='k')
plt.xlabel('Year',color='k')
handles, labels = a.get_legend_handles_labels()
a.xaxis.grid(False)
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(0.9, -0.16), loc='best', ncol=2, fontsize='x-large')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
