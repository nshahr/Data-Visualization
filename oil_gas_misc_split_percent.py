import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig, ax = plt.subplots()
df = pd.read_excel('oil_gas_misc_split_percent.xlsx')

mycolors = ['saddlebrown', 'coral', '#ffbf00']
a = df.plot(x = 'Date', y=[
    '% Crude Oil',
    '% Misc',
    '% Natural Gas',
    
], kind="area", color=mycolors, alpha=0.9, ax=ax)

for line in a.lines:
    line.set_linewidth(0)
handles, labels = a.get_legend_handles_labels()
a.xaxis.grid(False)
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1.05, -.15), loc='best', ncol=5, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in vals])
plt.ylabel("Weekly Rig Count",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
