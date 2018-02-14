import pandas as pd
from ggplot import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('by contractor.csv')
df.dropna()
df = df.iloc[::-1]
mycolors = ['#f96200','#fa6a0d','#fa721a','#fb7a27','#fb8234','#fbba41','#fc924f','#fc9a5c','#fda269','#fdaa77','#fdb284','#febb91','#fec39f','#ffccad']
a = df.plot(x = 'Date', y=['Patterson-UTI Drilling Company, LLC','Nabors Drilling USA, LP','Helmerich & Payne International Drlg Co',\
                            'Cactus Drilling Company, LLC','Precision Drilling (US) Corporation',\
                            'Sidewinder Drilling, LLC','SWN Drilling Company','Falcon Drilling Company, LLC',\
                            'Pioneer Energy Services Corp.','Scandrill, Inc.','Independence Contract Drilling, Inc.',\
                            'Basin Drilling, LP','Unit Drilling Company','Fountain Quail Drilling, LLC']\
                            , kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(2)
a.legend(bbox_to_anchor=(1, 1), loc='best', ncol=1)

plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("Rigs",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()