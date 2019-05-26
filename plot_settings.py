plot_setting = {}

default_bar_color = [
    'rgba(255, 133, 0, 1)',  # base orange color
    'rgba(255, 172, 83, 1)',  # light orange
    'rgba(211, 110, 0, 1)'  # dark orange
]

pc1 = [
    'rgba(7, 167, 229, 1)',  # base blue-ish color
    'rgba(81, 189, 230, 1)',  # light blue-ish
    'rgba(2, 97, 133, 1)'  # dark blue-ish
]

pc2 = [
    'rgba(238, 0, 166, 1)',  # base magenta color
    'rgba(238, 77, 175, 0.7)',  # light magenta
    'rgba(160, 0, 112, 1)'  # dark magenta
]

pc3 = [
    'rgba(0, 175, 59, 1)',  # base green color
    'rgba(77, 223, 127, 0.9)',  # light green
    'rgba(0, 98, 33, 1)'  # dark green
]

pc4 = [
    'rgba(255, 40, 0, 1)',  # base green color
    'rgba(255, 114, 88, 1)',  # light green
    'rgba(133, 21, 0, 1)'  # dark green
]


priority_colors = [pc1, pc2, pc3, pc4]

# primary_gadget_color = ()
# secondary_gadget_color = ()
# tertiary_gadget_color = ()
# quaternary_gadget_color = ()

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
plot_setting['priority_colors'] = priority_colors
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
