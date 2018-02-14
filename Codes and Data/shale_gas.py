import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('shale_gas_201706.csv')
df.dropna()
mycolors = ['coral', 'limegreen', 'b', 'peru', 'teal', 'pink', 'orange', 'darkviolet', 'g', 'steelblue','r']
a = df.plot(x = 'Date', y=['Antrim (MI, IN & OH)','Bakken (ND & MT)', 'Woodford (OK)', 'Barnett (TX)', 'Fayetteville (AR)', 'Eagle Ford (TX)', 'Haynesville (LA & TX)', 'Utica (OH, PA & WV)', 'Permian (TX & NM)', 'Rest of US shale', 'Marcellus (PA, WV, OH & NY)'], kind="area", color=mycolors, alpha=0.5)

for line in a.lines:
    line.set_linewidth(2)
handles, labels = a.get_legend_handles_labels()
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1, 0.9), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Cubic Feet per Day (Bcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
