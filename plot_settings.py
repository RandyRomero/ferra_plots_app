plot_setting = {}

default_bar_colors = [
    'rgba(255, 133, 0, 1)',  # base orange color
    'rgba(255, 172, 83, 1)',  # light orange
    'rgba(211, 110, 0, 1)'  # dark orange
]

highlight_colors = [
    'rgba(7, 167, 229, 1)',  # base blue-ish color
    'rgba(81, 189, 230, 1)',  # light blue-ish
    'rgba(2, 97, 133, 1)'  # dark blue-ish
]

geek_bench4 = {'traces_names': ('Все ядра', 'Одно ядро'),
               'title': 'Мощность процессора (тест GeekBench 4), баллы'}

sling_shot_extreme = {'title': 'Игровая производительность (тест 3DMark Sling Shot Extreme), баллы',
                      'traces_names': ('баллы',)}

antutu7 = {'title': 'Производительность всей системы (тест Antutu Benchmark 7), баллы',
           'traces_names': ('баллы',)}

battery_test = {'title': 'Время автономной работы, минуты',
                'traces_names': ('Чтение', 'Видео', 'Игры')
                }

plot_setting['default_bar_colors'] = default_bar_colors
plot_setting['highlight_colors'] = highlight_colors
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
