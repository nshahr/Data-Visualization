import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
import datetime
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig, ax = plt.subplots(sharex=True, figsize=(8.5, 4.8))
fig_size = plt.rcParams["figure.figsize"]

df = pd.read_csv('U.S._Natural_Gas_Exports.csv')
df.dropna()
df = df.iloc[::-1]
print(df.columns)
mycolors = ['saddlebrown', '#3b5998', '#ffbf00']
a = df.plot(x = 'Month', y=['U.S. LNG Exports',\
                            'U.S. Natural Gas Pipeline Exports to Mexico',\
                            'U.S. Natural Gas Pipeline Exports to Canada',\
                             ], kind="area", color=mycolors, alpha=0.88, ax=ax)
for line in a.lines:
    line.set_linewidth(0)
a.xaxis.grid(False)
handles, labels = a.get_legend_handles_labels()
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(.85, -0.115), loc='best', ncol=1, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)  
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet per Day (Bcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
