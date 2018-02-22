import plotly.plotly as py
import plotly
import pandas as pd
from os import path
import plotly.graph_objs as go
df = pd.read_csv('map.csv')

dff = pd.read_csv('gasreserves.csv')

limits = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)]
colors = [
    '#d11141',
    '#00aedb',
    '#f37735',
    '#800080',
    '#00b159',
    '#011f4b',
    '#845422',
    '#ffc425',
    '#000dff'
]
cities = []
scale = 16

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        sizemode = 'diameter',
        marker = dict( 
            size = df_sub['Value']/scale, 
            color = colors[i],
            line = dict(width = 2)
        ),
        name = '{0} - {1}'.format(lim[0],lim[1]) )
    cities.append(city)

# ttext = go.Scattergeo(
#     type = 'scattergeo',
#     mode = 'text',
#     locationmode = 'USA-states',
#     lon = dff['lon'],
#     lat = dff['lat'],
#     text = dff['code']+'<br>'+dff['text'].str.strip(".0"),
#     textfont=dict(color='white',size=9)
    # )

layout = dict(
        title = '2014 US city populations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',       
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"           
        ),  
    )

fig = dict( data=cities, layout=layout )
plotly.offline.plot(fig, validate=False, filename=path.basename(__file__)+".html")