import os
from pprint import pprint

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
import plotly.io as pio

from config import path_to_orca
from prepare_data import prepare_data
from plot_settings import plot_setting as ps

init_notebook_mode(connected=True)

if not os.path.exists('images'):
    os.mkdir('images')

# todo make it accept command line arguments

pio.orca.config.executable = path_to_orca


def make_chart(bench, smartphones):
    print('Start preparing data for a plot...')
    data = prepare_data(bench, smartphones)

    print('Start making the plot...')
    y_axis_names = data[0]
    length = len(y_axis_names)

    traces = []
    if len(data) == 4:
        ps['default_bar_color'].rotate(1)
        print(ps['default_bar_color'])

    for i, x_axis in enumerate(data[1:]):
        trace = go.Bar(
            x=x_axis,
            y=y_axis_names,
            text=x_axis,
            textfont={'color': ['#ffffff'] * length, 'size': [20] * length},
            textposition='auto',
            name=ps[bench]['traces_names'][i],
            orientation='h',
            marker=dict(
                color=ps['default_bar_color'][i]
            )
        )

        traces.append(trace)

    layout = go.Layout(title=ps[bench]['title'],
                       titlefont=ps['layout_settings']['titlefont'],
                       margin=ps['layout_settings']['margin'],
                       barmode='stack',
                       legend=ps['layout_settings']['legend'],
                       xaxis=dict(tickfont=ps['layout_settings']['tickfont']),
                       yaxis=dict(tickfont=ps['layout_settings']['tickfont'],
                                  showticklabels=True))

    fig = go.Figure(data=traces, layout=layout)

    print('Start rendering the plot...')
    # pio.write_image(fig, 'images/GeekBench.png', width=1366, height=(1366 * 2))
    pio.write_image(fig, f'images/{bench}.png', width=1366, height=1366)
    print(f'Plot was saved as images/{bench}.png')


    # color1 = [default_bar_color1] * length
    # color2 = [default_bar_color2] * length
    #
    # # blue-ish
    # color1[15] = 'rgba(7, 118, 160, 1)'
    # color2[15] = 'rgba(43, 132, 166, 1)'