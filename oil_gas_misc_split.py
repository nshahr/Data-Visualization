import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})

df = pd.read_excel('oil_gas_misc_split.xlsx')
print(df.columns)
mycolors = ['saddlebrown', 'coral', '#ffbf00']
a = df.plot(x = 'Date', y=['Crude Oil', 'Misc', 'Natural Gas'], kind="area", color=mycolors, alpha=0.9)

for line in a.lines:
    line.set_linewidth(0)
handles, labels = a.get_legend_handles_labels()
a.xaxis.grid(False)
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(0.98, -0.15), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Weekly Rig Count",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
