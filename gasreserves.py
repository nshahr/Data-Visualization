import pandas as pd
import plotly as py
import numpy as np
import plotly.graph_objs as go
from os import path


df = pd.read_csv('gasreserves.csv')
df['Value'] = df['Value'].apply(pd.to_numeric, errors='coerce')
print df.head()
print df.dtypes

df['text'] = df['Value'].astype(str)
df['text'].replace('nan', '*', inplace=True)
df['text'].replace('0.0', '', inplace=True)
colors = ["#89ccB3","#70c1a6","#4Bab8e","#08755B","#006B53"]
scl = [[0.0, colors[0]],[0.12, colors[2]],\
            [0.5, colors[4]],[1.0, colors[3]]]

city = go.Choropleth(
    type = 'choropleth',
    locationmode = 'USA-states',
    text = df['code']+'<br>'+df['text'],
    locations = df['code'],
    z = df['Value'].astype(float),
    colorscale = scl,
    marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Billion Cubic Feet")
        ) 

text = go.Scattergeo(
    type = 'scattergeo',
    mode = 'text',
    locationmode = 'USA-states',
    lon = df['lon'],
    lat = df['lat'],
    text = df['code']+'<br>'+df['text'].str.strip(".0"),
    textfont=dict(color='white',size=9)
    )



layout = dict(
        title = 'U.S. Lower 48 Natural Gas Proved Reserves By State/Area, 2015',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            showlake = False,
            lakecolor = 'rgb(255, 255, 255)',
            landcolor = 'rgb(255, 255, 255)',
        ),
    )
data = [city, text]
fig = dict( data=data, layout=layout )
py.offline.plot(fig, validate=False, filename=path.basename(__file__)+".html")

