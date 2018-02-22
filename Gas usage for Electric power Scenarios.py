import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 10})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 4.2
df = pd.read_csv('Gas usage for Electric power Scenarios.csv')
df.dropna()
df = df.iloc[::-1]
print(df.columns)
mycolors = ['r', '#6b3d4b', 'orange', 'gray', 'c', 'y', 'g', '#62513b']
a = df.plot(x = 'Year', y=[
    'High Oil and Gas Resource and Technology',
    'High Economic Growth',
    'Low Oil Price',
    'Reference Case',
    'Low Economic Growth',
    'High Oil Price',
    'Reference Case Without Clean Power Plan',
    'Low Oil and Gas Resource and Technology',
], kind="line", color=mycolors)
for line in a.lines:
    line.set_linewidth(1.5)
a.xaxis.grid(False)
a.legend(bbox_to_anchor=(1.05, -0.12), loc='best', ncol=2, fontsize='x-large')
plt.tick_params(axis='x', labelsize=9)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Kilowatt Hours (Bkwh)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
