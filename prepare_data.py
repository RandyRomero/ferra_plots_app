import csv
from datetime import datetime
from dataclasses import dataclass
import re
from typing import Optional, List

import openpyxl

from config import path_to_excel_workbook


class Smartphones:
    def __init__(self):
        self.all_smartphones: Optional[List[Smartphone]] = []
        # self.benchmarks_dict = {'GeekBench 4': self._from_geekbench4_table,
        #                         '3DMark Sling Shot Extreme': self._from_sling_shot_and_antutu_tables,
        #                         'battery_test': self._from_battery_test_table}

    @staticmethod
    def open_sheet(sheet_name):
        wb = openpyxl.load_workbook(path_to_excel_workbook)
        return wb[sheet_name]

    def _from_geekbench4_table(self):
        table_start_row = 12
        the_last_row= 1048576
        sheet = self.open_sheet('GeekBench 4')
        i = 0
        for row in range(table_start_row, the_last_row, 1):
            if sheet.cell(row=row, column=32).value:
                raw_date = sheet.cell(row=row, column=31).value
                date = raw_date.date() if raw_date else None
                name = sheet.cell(row=row, column=33).value
                all_cpu_scores = sheet.cell(row=row, column=34).value
                one_cpu_score = sheet.cell(row=row, column=35).value
                i += 1
                print(f'{i}. {date}, {name}, {all_cpu_scores}, '
                      f'{one_cpu_score}.')

                smartphone = Smartphone.from_list(date, name)
                geek_bench4 = GeekBench4(smartphone, all_cpu_scores,
                                         one_cpu_score)
                smartphone.geek_bench4 = geek_bench4
                self.all_smartphones.append(smartphone)
            else:
                print('Done working on GeekBench 4 table')
                return

    def _from_sling_shot_and_antutu_tables(self):
        pass

    def _from_battery_test_table(self):
        pass

    def from_smartphone_bench_excel_book(self):
        self._from_geekbench4_table()


class GeekBench4:

    def __init__(self, smartphone, all_cores_score, one_cores_score):

        self.smartphone: Smartphone = smartphone
        self.all_cores_score: int = all_cores_score
        self.one_cores_score: int = one_cores_score
        self.total_score: int = all_cores_score + one_cores_score


class Antutu7:

    def __init__(self, smartphone, score):
        self.smartphone: Smartphone = smartphone
        self.score = score


class SlingShotExtreme:
    """
    3DMark Sling Shot Extreme benchmark
    """

    def __init__(self, smartphone, score):
        self.smartphone: Smartphone = smartphone
        self.score = score


class BatteryTest:
    def __init__(self, smartphone, movie_score, read_score, game_score):
        self.smartphone: Smartphone = smartphone
        self.movie_score = movie_score
        self.read_score = read_score
        self.game_score = game_score
        self.total_score = movie_score + read_score + game_score


class Smartphone:
    def __init__(self, date: datetime, name, chip, battery_capacity=None,
                 geek_bench4: Optional[GeekBench4] = None,
                 sling_shot_extreme: Optional[SlingShotExtreme] = None,
                 antutu7: Optional[Antutu7] = None,
                 battery_test: Optional[BatteryTest] = None):

        self.date = date
        self.name: str = name
        self.chip: str = chip
        self.battery_capacity: int = battery_capacity
        self.geek_bench4 = geek_bench4
        self.sling_shot_extreme = sling_shot_extreme
        self.antutu_7 = antutu7
        self.battery_test = battery_test

    @classmethod
    def from_list(cls, date, name):
        date = date if date else None
        regex = re.compile(r'^(.*)\((.*)\)')
        matches = re.search(regex, name).groups()
        name, chip = matches[0].strip(), matches[1].strip()
        smartphone = cls(date, name, chip)
        return smartphone


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


def main():
    smartphones = Smartphones()
    smartphones.from_smartphone_bench_excel_book()
    for smartphone in smartphones.all_smartphones:
        print(smartphone.geek_bench4.total_score)


if __name__ == '__main__':
    main()