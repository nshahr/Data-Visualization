import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 4.7
df = pd.read_csv('by county.csv')
df.dropna()
df = df.iloc[::-1]
mycolors = ['#700085','#75098a','#7b138f','#811d94','#872799','#8d319e','#933ba3','#9845a8','#9e4fad','#a459b2','#aa63b7','#b06dbc','#b677c1','#bb81c6','#c18bcb','#c795d0','#cd9fd5','#D3a9da','#d9b3e0']
a = df.plot(x = 'Date', y=['DE SOTO','WASHINGTON','LINCOLN','EDDY','BELMONT','WELD','JEFFERSON','RED RIVER','GREENE','PANOLA','SUSQUEHANNA','WEBB','CADDO','GRADY','HEMPHILL','PITTSBURG','RUSK','BOSSIER','COAL'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(1)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1.04, 1.2), loc='best', ncol=1, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Rigs",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()