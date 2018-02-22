import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')

# Algonquin = 'Algonquin_Citygates_Completed'
# Chicago = 'Chicago_Citygates_Completed'
# Henry = 'Henry_Completed'
# Malin = 'Malin_Completed'
# PG = 'PG&E_Completed'
# Socal_Citygate = 'Socal_Citygate_Completed'
# Socal_Ehrenberg = 'Socal_Ehrenberg_Completed'
# TETCO = 'TETCO_M3_Completed'

# Algonquin_df = pd.read_csv(Algonquin+'.csv')
# Algonquin_df['file_name'] = Algonquin
# Chicago_df = pd.read_csv(Chicago+'.csv')
# Chicago_df['file_name'] = Chicago
# Henry_df = pd.read_csv(Henry+'.csv')
# Henry_df['file_name'] = Henry
# Malin_df = pd.read_csv(Malin+'.csv')
# Malin_df['file_name'] = Malin
# PG_df = pd.read_csv(PG+'.csv')
# PG_df['file_name'] = PG
# Socal_Citygate_df = pd.read_csv(Socal_Citygate+'.csv')
# Socal_Citygate_df['file_name'] = Socal_Citygate
# Socal_Ehrenberg_df = pd.read_csv(Socal_Ehrenberg+'.csv')
# Socal_Ehrenberg_df['file_name'] = Socal_Ehrenberg
# TETCO_df = pd.read_csv(TETCO+'.csv')
# TETCO_df['file_name'] = TETCO

# df = pd.concat([Algonquin_df, Chicago_df, Henry_df, Malin_df, PG_df, Socal_Citygate_df, Socal_Ehrenberg_df, TETCO_df])
# dff = df.pivot(index='Date', columns='file_name', values='Wtd avg price $/MMBtu')
# dff.to_csv('total_hub.csv')

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=False, figsize=(13, 10))
df = pd.read_csv('total_hub_complete.csv')
df2 = pd.read_csv('total_hub_complete2.csv')

mycolors = [
    '#d11141',
    '#00aedb',
    '#f37735',
    '#800080',
    '#00b159',
    '#011f4b',
    '#845422',
    '#ffc425',
]
a = df.plot(x = 'Date', y=['Algonquin_Citygates',\
                            'Chicago_Citygates',\
                            'Henry',\
                            'Malin',\
                            'PG&E',\
                            'Socal_Citygate',\
                            'Socal_Ehrenberg',\
                            'TETCO_M3'], kind="line",stacked=False,color=mycolors,\
                            subplots=False, ax=axes[0])
a.legend(bbox_to_anchor=(0.9, -1.3), loc='best', ncol=3, fontsize='x-large')

b = df2.plot(x = 'Date', y=['Algonquin_Citygates',\
                            'Chicago_Citygates',\
                            'Henry',\
                            'Malin',\
                            'PG&E',\
                            'Socal_Citygate',\
                            'Socal_Ehrenberg',\
                            'TETCO_M3'], kind="line",stacked=False,color=mycolors,\
                            subplots=False, ax=axes[1], legend=False)


axes[0].set_xlabel("Date", color='black')
axes[1].set_xlabel("Date", color='black')
axes[0].tick_params(axis='x', labelsize=10.5, color='black')
axes[1].tick_params(axis='x', labelsize=10.5, color='black')
axes[0].xaxis.grid(False)
axes[1].xaxis.grid(False)
plt.ylabel("U.S. Dollars per Million British Thermal Unit ($/MMBtu)",color='black',verticalalignment='bottom',horizontalalignment='left',position=(4,0.5))
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
