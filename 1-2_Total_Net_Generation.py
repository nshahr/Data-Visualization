import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
from datetime import datetime
style.use('ggplot')
rcParams.update({'font.size': 10})
# fig, ax = plt.figure()
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 4.2
plt.rcParams["figure.figsize"] = fig_size

print(fig_size)
df = pd.read_csv('1-2_Total_Net_Generation.csv')
df['Date'] = df.apply(lambda row: datetime(row['Year'], row['Month'], 1), axis=1)
mycolors = ['dimgrey', 'gold', 'saddlebrown', 'dodgerblue', 'deeppink']
a = df.plot(x = 'Date', y=['Other','Hydroelectric', 'Coal', 'Natural Gas', 'Nuclear'], kind="area", color=mycolors[::-1], alpha=0.9)

for line in a.lines:
    line.set_linewidth(0)

a.xaxis.grid(False)
handles, labels = a.get_legend_handles_labels()
a.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1.07, -.14), loc='best', ncol=5, fontsize='x-large')
plt.tick_params(axis='x', labelsize=9)
plt.xlabel("Date", color='black')
plt.ylabel("Billion Kilowatt Hours (Bkwh)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()