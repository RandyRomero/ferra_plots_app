from collections import deque

plot_setting = {}

default_bar_color = deque([
    'rgba(255, 133, 0, 1)',
    'rgba(255, 160, 57, 1)',
    'rgba(211, 110, 0, 1)'
])

primary_gadget_color = ()
secondary_gadget_color = ()
tertiary_gadget_color = ()
quaternary_gadget_color = ()

geek_bench4 = {'traces_names': ('Все ядра', 'Одно ядро'),
               'title': 'Мощность процессора (тест GeekBench 4), баллы'}

sling_shot_extreme = {'title': 'Игровая производительность (тест 3DMark Sling Shot Extreme), баллы',
                      'traces_names': ('баллы',)}

antutu7 = {'title': 'Производительность всей системы (тест Antutu Benchmark 7), баллы',
           'traces_names': ('баллы',)}

battery_test = {'title': 'Время автономной работы, минуты',
                'traces_names': ('Чтение', 'Видео', 'Игры')
                }

plot_setting['default_bar_color'] = default_bar_color
plot_setting['primary_gadget_color '] = primary_gadget_color
plot_setting['tertiary_gadget_color'] = tertiary_gadget_color
plot_setting['quaternary_gadget_color'] = quaternary_gadget_color
plot_setting['geek_bench4'] = geek_bench4
plot_setting['sling_shot_extreme'] = sling_shot_extreme
plot_setting['antutu7'] = antutu7
plot_setting['battery_test'] = battery_test

layout_settings = {'titlefont': {'size': 36},
                   'margin': {'pad': 15, 'l': 450},
                   'legend': {'font': {'size': 20}, 'orientation': 'h'},
                   'tickfont': {'size': 20}
                   }

plot_setting['layout_settings'] = layout_settings

# default_bar_color1 = 'rgba(255, 133, 0, 1)'
# default_bar_color2 = 'rgba(255, 160, 57, 1)'