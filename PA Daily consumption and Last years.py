import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 5
print(fig_size)
df = pd.read_csv('PA Daily consumption and Last years -fixed data.csv')
fig, ax = plt.subplots(figsize=(8,5), sharex=True)

# df = df.iloc[::-1]
df.plot(x = 'Date', y='Daily Predicted', kind="line", color='b', ax=ax, legend=True)

df.plot(x = 'Date', y='Real Average Monthly/30', linestyle='-', marker='o', ax=ax, color='r',legend=True)

dff = pd.read_csv('PA Daily consumption and Last years -fixed data.csv')
dff.dropna(inplace=True)
dff.plot(y='Real Average Monthly/30', kind='line', ax=ax, lw=1, legend=False, color='r')

ax.xaxis.grid(False)
plt.legend(bbox_to_anchor=(1.2, -0.15), loc='best', ncol=3, fontsize='x-large')
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Million Cubic Feet per Day (MMcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
