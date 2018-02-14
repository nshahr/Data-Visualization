import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 9})

df = pd.read_csv('PA Daily consumption and Last years -fixed data.csv')
fig, ax = plt.subplots(figsize=(8,5), sharex=True)

# df = df.iloc[::-1]
df.plot(x = 'Date', y='Daily Predicted', kind="line", color='b', ms=10, ax=ax, lw=1, legend=True)

df.plot(x = 'Date', y='Real Average Monthly/30', linestyle='-', marker='o', ax=ax, color='r',legend=True)

dff = pd.read_csv('PA Daily consumption and Last years -fixed data.csv')
dff.dropna(inplace=True)
dff.plot(y='Real Average Monthly/30', kind='line', ax=ax, lw=1, legend=False, color='r')

plt.legend(bbox_to_anchor=(1, 0.65), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=8)
plt.xlabel("Date", color='black')
plt.ylabel("Million Cubic Feet per Day (MMcf/d)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
