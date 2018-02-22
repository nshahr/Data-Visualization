import pandas as pd
import plotly as py
import numpy as np
from plotly.graph_objs import *
from os import path

trace1 = Choropleth(
    z=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    showlegend=True,
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, '#a0db8e']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['AL','FL','GA','MS','NC','SC','TN'],
    name='Southeast',
    text='Southeast',
    showscale=False,
    zauto=False,
    zmax=1,
    zmin=0,
    marker=dict(line=dict(color='white')),
    
)
trace2 = Choropleth(
    z=['1', '1'],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(255,167,0)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['LA','TX'],
    name='Gulf',
    showscale=False,
    zauto=False,
    zmax=1,
    zmin=0,
    marker=dict(line=dict(color='white'))
)
trace3 = Choropleth(
    z=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1','1','1','1'],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(141,85,36)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['AR','IL','IN','IA','KS','MI','MN','MO','NE','ND','OK','SD','WI'],
    name='Midwest',
    text='Midwest',
    showscale=False,
    zauto=False,
    zmax=1,
    zmin=0,
    marker=dict(line=dict(color='white'))
)

trace4 = Choropleth(
    z=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1','1','1','1','1','1'],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, 'rgb(241,194,125)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['CT','KY','ME','MA','NH','NJ','NY','OH','PA','RI','VT','DE','MD','VA','WV'],
    name='Northeast',
    legendgroup='Northeast',
    showscale=False,
    zauto=False,
    zmax=1,
    zmin=0,
    marker=dict(line=dict(color='white'))
)

trace5 = Choropleth(
    z=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255,255,255)'], [1, '#7aceeb']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['AZ','CA','CO','ID','MT','NV','NM','OR','UT','WA','WY'],
    name='Western',
    showscale=False,
    zauto=False,
    zmax=1,
    zmin=0,
    marker=dict(line=dict(color='white')),
    showlegend=True
)

layout = Layout(
    geo=dict(
        countrycolor='rgb(102, 102, 102)',
        countrywidth=0.1,
        lakecolor='rgb(255, 255, 255)',
        landcolor='rgba(255, 255, 255, 0.28)',
        lonaxis=dict(
            gridwidth=1.5999999999999999,
            range=[-180, -50],
            showgrid=False
        ),
        projection=dict(
            type='albers usa'
        ),
        scope='usa',
        showland=True,
        showrivers=False,
        showsubunits=True,
    ),
    
    showlegend=True,
    title='Federal Energy Regulatory Commission (FERC) Natural Gas Market Classification',
    legend = dict(
           traceorder = 'reversed'
    )
)
fig = dict( data=([trace1, trace2, trace3, trace4, trace5]), layout=layout )
# py.plotly.image.save_as(fig, filename='US_map.png')
py.offline.plot(fig, validate=False, filename=path.basename(__file__)+".html")

