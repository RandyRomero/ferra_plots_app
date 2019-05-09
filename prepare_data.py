import csv
from datetime import datetime
import re


class Smartphone:
    def __init__(self, date, total_score, name, chip, all_cores_score,
                 one_core_score):

        self.date = date
        self.total_score = total_score
        self.name = name
        self.chip = chip
        self.all_cores_score = all_cores_score
        self.one_cores_score = one_core_score

    @classmethod
    def from_list(cls, row):
        date = datetime.strptime(row[0], '%d.%m.%Y') if row[0] else None

        total_score = int(row[1])

        regex = re.compile(r'^(.*)\((.*)\)')
        matches = re.search(regex, row[2]).groups()
        name, chip = matches[0].strip(), matches[1].strip()

        all_cores_score = int(row[3])
        one_core_score = int(row[4])

        return cls(date.date() if date else None, total_score,
                   name, chip, all_cores_score, one_core_score)

    def __str__(self):
        return (f'{self.name} on {self.chip} with total score of ' 
                f'{self.total_score} in GeekBench 4. Tested on {self.date}')


def prepare_data():
    raw_data = csv.reader(open('sources_for_charts/GeekBench4.csv'))
    smartphones = [Smartphone.from_list(s) for s in raw_data]
    smartphones.sort(key=lambda x: x.total_score)

    y_axis_names = []
    x_axis_values = []
    x_axis_values2 = []

    for smartphone in smartphones:
        y_axis_names.append(f'{smartphone.name} ({smartphone.chip})')
        x_axis_values.append(smartphone.all_cores_score)
        x_axis_values2.append(smartphone.one_cores_score)

    return y_axis_names, x_axis_values, x_axis_values2