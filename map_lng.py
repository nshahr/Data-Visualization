import plotly.plotly as py
import plotly
import pandas as pd
from os import path
import plotly.graph_objs as go
df = pd.read_excel('map_lng.xlsx')

colors = ['green', 'gold', '#d11141',]
approveds = []
proposeds = []
existings = []

for i in range(13,23):
    approved = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df[ df['NO']==i ]['Lon'],
        lat = df[ df['NO' ]==i ]['Lat'],
        text = df[ df['NO'] == i ]['NO'],
        sizemode = 'diameter',
        mode = 'markers+text',
        textposition = 'bottom center',
        marker = dict( 
            color = colors[1],
            size = 10
            # line = dict(width = 2)
        ))
    approveds.append(approved)

for i in range(23,38):
    proposed = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df[ df['NO']==i ]['Lon'],
        lat = df[ df['NO' ]==i ]['Lat'],
        text = df[ df['NO'] == i ]['NO'],
        sizemode = 'diameter',
        mode = 'markers+text',
        textposition = 'bottom center',
        marker = dict( 
            color = colors[2],
            size = 10
            # line = dict(width = 2)
        ))
    proposeds.append(proposed)


for i in range(1,13):
    exists = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df[ df['NO']==i ]['Lon'],
        lat = df[ df['NO' ]==i ]['Lat'],
        text = df[ df['NO'] == i ]['NO'],
        sizemode = 'diameter',
        mode = 'markers+text',
        textposition = 'bottom center',
        marker = dict( 
            color = colors[0],
            size = 10
            # line = dict(width = 2)
        ))
    existings.append(exists)
layout = dict(
        title = 'U.S. LNG Import/Export Terminals',
        showlegend = True,
        geo = dict(
            scope='usa',
            # projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',       
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"           
        ),  
    )
fig = dict( data=existings+approveds+proposeds, layout=layout )
plotly.offline.plot(fig, validate=False, filename=path.basename(__file__)+".html")