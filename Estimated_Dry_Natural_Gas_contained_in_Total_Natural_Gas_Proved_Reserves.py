import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import style
from os import path
style.use('ggplot')
rcParams.update({'font.size': 12})
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 5
df = pd.read_csv('Estimated_Dry_Natural_Gas_contained_in_Total_Natural_Gas_Proved_Reserves.csv')
df = df[::-1]
mycolors = ["Gold","#78b9d8","r","#653bb6","#d2d840","b","#5ed98e",\
            "#a6417f","#67a137","#7174ce","#d59e33","coral","#b4d97f","#d34461",\
            "#86dbc3","#682b2a","#d7bf79","#5c6d8e","#bd6a3e","#ca99d0","#437133","#c18082","#363b31","#d1c6b9","#7e6c33","#5e8f7b"]
a = df.plot(x = 'Date',\
            y=["Alabama",\
            "Gulf of Mexico Federal Offshore-Texas",\
            "California Federal Offshore",\
            "Florida",\
            "Ohio",\
            "North Dakota",\
            "California",\
            "Michigan",\
            "Montana",\
            "Kansas",\
            "Mississippi",\
            "Virginia",\
            "Kentucky",\
            "New York",\
            "Miscellaneous States",\
            "Utah",\
            "Arkansas",\
            "Gulf of Mexico Federal Offshore-Louisiana and Alabama",\
            "New Mexico",\
            "Louisiana",\
            "Colorado",\
            "Oklahoma",\
            "West Virginia",\
            "Pennsylvania",\
            "Wyoming",\
            "Texas",\
            ],kind="area", color=mycolors[::-1], figsize=(16,12), alpha=0.9)

handles, labels = a.get_legend_handles_labels()
a.legend(reversed(handles), reversed(labels),bbox_to_anchor=(1, 0.9), loc='best', ncol=1, fontsize='large')
a.xaxis.grid(False)
plt.tick_params(axis='x', labelsize=11)
plt.xlabel("Date", color='black')
plt.ylabel("Trillion Cubic Feet (Tcf)",color='black')
plt.savefig(path.basename(__file__)+".png",bbox_inches='tight')
# plt.show()
