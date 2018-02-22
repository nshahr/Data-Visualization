import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 9
fig_size[1] = 4.8
df = pd.read_excel('Shale productivity2.xlsx')

mycolors = ['g', 'gold', 'coral', 'indigo', 'pink', 'teal', '#fe5757',]
a = df.plot(x = 'Date', y=[
    'Permian Shale Play',
    'Bakken Shale Play',
    'Anadarko Shale Play',
    'Niobrara Shale Play',
    'Eagle Ford Shale Play',
    'Haynesville Shale Play',
    'Appalachia Shale Play',
], kind="area", color=mycolors, alpha=0.93)

for line in a.lines:
    line.set_linewidth(0)
a.xaxis.grid(False)    
handles, labels = a.get_legend_handles_labels()
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1.05, -0.11), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Million Cubic Feet per Day (MMcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
