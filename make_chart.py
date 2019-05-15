import os

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
import plotly.io as pio

from config import path_to_orca
from prepare_data import prepare_data
init_notebook_mode(connected=True)

if not os.path.exists('images'):
    os.mkdir('images')

# todo make it accept command line arguments

pio.orca.config.executable = path_to_orca

print('Start preparing data for a plot...')
y_axis_names, x_axis_values, x_axis_values2 = prepare_data()

print('Start making the plot...')
length = len(y_axis_names)

trace1 = go.Bar(
    x=x_axis_values,
    y=y_axis_names,
    text=x_axis_values,
    textfont={'color': ['#ffffff'] * length, 'size': [15] * length},
    textposition='auto',
    name='Все ядра',
    orientation='h',
    marker=dict(
        color='rgba(255, 133, 0, 1)'
    )
)
trace2 = go.Bar(
    y=y_axis_names,
    x=x_axis_values2,
    text=x_axis_values2,
    textfont={'color': ['#ffffff'] * length, 'size': [15] * length},
    textposition='auto',
    name='Одно ядро',
    orientation='h',
    marker=dict(
        color='rgba(255, 172, 63, 1)'
    )
)

data = [trace1, trace2]
layout = go.Layout(title='Geekbench 4',
    barmode='stack',
    legend={'font': {'size': 16}},
     yaxis=dict(
        showticklabels=True,
        tickfont=dict(
            size=14
        ),
    ))

fig = go.Figure(data=data, layout=layout)
fig['layout']['margin'] = {'l': 350}

print('Start rendering the plot...')
pio.write_image(fig, 'images/GeekBench.png', width=1366, height=(1366 * 2))
print('Plot was saved as images/GeekBench.png')
