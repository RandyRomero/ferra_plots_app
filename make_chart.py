import os

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
import plotly.io as pio

from config import path_to_orca
from prepare_data import prepare_data
from plot_settings import plot_setting as ps

init_notebook_mode(connected=True)

if not os.path.exists('images'):
    os.mkdir('images')


pio.orca.config.executable = path_to_orca


def make_chart(bench, smartphones):
    print(f'Start preparing data for a {bench} plot...')
    axes, highlighted_smartphones = prepare_data(bench, smartphones)

    print('Start making the plot...')
    y_axis_names = axes[0]
    axis_length = len(y_axis_names)
    default_colors = ps['default_bar_colors']
    highlight_colors = ps['highlight_colors']
    traces = []

    # We have to change the order of colors in case there are more than two
    # colors needed. Basically we shift list so as them start with the last
    # value instead of the first
    if len(axes) == 4:
        default_colors = default_colors[-1:] + default_colors[:-1]
        highlight_colors = highlight_colors[-1:] + highlight_colors[:-1]

    for i, value in enumerate(axes[1:]):

        # here we set default colors for each bar at first, then special colors
        # to highlight smartphones of interest
        colors = [default_colors[i]] * axis_length
        for smartphone_index in highlighted_smartphones:
            colors[smartphone_index] = highlight_colors[i]

        trace = go.Bar(
            x=value,
            y=y_axis_names,
            text=value,
            textfont={'color': ['#ffffff'] * axis_length,
                      'size': [20] * axis_length},
            textposition='auto',
            name=ps[bench]['traces_names'][i],
            orientation='h',
            marker=dict(
                color=colors
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
    print(f'Start rendering the {bench} plot...')
    pio.write_image(fig, f'images/{bench}.png', width=1366, height=1366)
    print(f'The plot was saved as images/{bench}.png')
