import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 6
df = pd.read_csv('by company.csv')
df.dropna()
df = df.iloc[::-1]
mycolors = ['#18008a','#230f90','#2f1e97','#3b2d9e','#4439a3','#4f47aa','#5a55b0','#6563b7','#7172bd','#7c80c3','#878eca','#929cd0','#9dabd7','#a8b9dd','#b3c7e4','#bed5ea','#cae4f1']
a = df.plot(x = 'Date', y=['BP, plc','EQT Corporation','Range Louisiana Operating, LLC',\
                            'Range Resources Corporation','Southwestern Energy Company',\
                            'Rice Energy, Inc.','Ascent Resources, LLC',\
                            'Gulfport Energy Corporation','Chesapeake Energy Corporation',\
                            'Anadarko Petroleum Corporation','Vine Oil & Gas, LP',\
                            'EXCO Resources, Inc.','GEP Haynesville, LLC',\
                            'Indigo Minerals, LLC','BHP Billiton, Limited',
                            'Exxon Mobil Corporation','Mewbourne Oil Company']
                            , kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(1)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1, 1.02), loc='best', ncol=1, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Rigs",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()