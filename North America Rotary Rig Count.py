import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 9
fig_size[1] = 4.9
df = pd.read_csv('North America Rotary Rig Count.csv')
print(df.columns)
mycolors = [
'#d37310',
'#4f88cf',
'#80d93a',
'#b62212',
'#132e11',
'#2d1616',
'#c2eb2f',
'#218a53',
'#9ed70a',
'#fdc689',
'#c13b27',
'#4b859f',
'#cba9bd',
'#5973e4',
'#1e3c18',
'#dcd1dd',
'#3c4438',
'#05e1f1',
'#f6e046',
'#8f93ad',
]
mycolors2 = ['coral', 'c', 'b', 'peru', 'indigo', '#f6e046', '#1e3c18', 'saddlebrown','g', 'limegreen', 'steelblue','pink', 'orange', 'r']
a = df.plot(x = 'Date', y=[
    'Williston Shale Play',
    'Ardmore Woodford Shale Play',
    'Arkoma Woodford Shale Play',
    'Mississippian Shale Play',
    'Utica Shale Play',
    'Fayetteville Shale Play',
    'DJ-Niobrara Shale Play',
    'Cana Woodford Shale Play',
    'Permian Shale Play',
    'Barnett Shale Play',
    'Granite Wash Shale Play',
    'Eagle Ford Shale Play',
    'Haynesville Shale Play',
    'Marcellus Shale Play',
    'Others Shale Play',

], kind="area", color=mycolors2, alpha=0.85)
a.xaxis.grid(False)
for line in a.lines:
    line.set_linewidth(0)
handles, labels = a.get_legend_handles_labels()
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1, 0.9), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Rig Count",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
