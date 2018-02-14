import pandas as pd
from ggplot import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})

df = pd.read_csv('stock_price.csv')
df.dropna()
# df = df.iloc[::-1]
mycolors = ['r', 'b', 'coral', 'darkviolet', 'pink', 'peru', 'limegreen']
a = df.plot(x = 'Date', y=['EQT US Equity COMMON', 'RRC US Equity COMMON',\
                             'NFG US Equity COMMON', 'CNX US Equity COMMON', 'CHK US Equity COMMON',\
                             'STO US Equity COMMON', 'AR US Equity COMMON'], kind="line", color=mycolors)

for line in a.lines:
    line.set_linewidth(0.7)
a.legend(bbox_to_anchor=(1, 0.7), loc='best', ncol=1)
plt.tick_params(axis='x', labelsize=7)
plt.xlabel("Date", color='black')
plt.ylabel("US Dollars",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()