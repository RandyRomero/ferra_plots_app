from datetime import datetime
import re
from typing import Optional, List, Tuple

import openpyxl

from config import path_to_excel_workbook


class Smartphones:
    def __init__(self):
        self.all_smartphones: Optional[List[Smartphone]] = []

    @staticmethod
    def open_sheet(sheet_name):
        wb = openpyxl.load_workbook(path_to_excel_workbook)
        return wb[sheet_name]

    def _from_geekbench4_table(self):

        # where my table with results of smartphones begins
        table_start_row = 12
        the_last_row = 1048576  # the last row in excel table
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


class Benchmark:

    name: str = 'Benchmark name here'
    subtests: Tuple[str] = ()

    def __init__(self, smartphone):
        self.smartphone: Smartphone = smartphone

    def make_list_of_bench_results(self):
        return [getattr(self, attr) for attr in dir(self) if 'score' in attr]

    def __str__(self):
        list_of_score_attributes = self.make_list_of_bench_results()
        response = (f'Smartphone {self.smartphone.name}, '
                    f'results in {__class__.name}:\n')
        response += f'Date: {self.smartphone.date}\n'

        for name, value in zip(GeekBench4.subtests, list_of_score_attributes):
            response += f'{name}: {value}\n'

        return response


class GeekBench4(Benchmark):

    name: str = 'GeekBench 4'
    subtests: Tuple[str] = ('Single-Core Score', 'Multi-Core Score',
                            'Total Score')

    def __init__(self, smartphone, all_cores_score, one_cores_score):
        super().__init__(smartphone)

        self.multi_core_score: int = all_cores_score
        self.single_core_score: int = one_cores_score
        self.total_score: int = all_cores_score + one_cores_score


class Antutu7(Benchmark):

    name: str = 'AnTuTu Benchmark 7'
    subtests: Tuple[str] = ('Total Score',)

    def __init__(self, smartphone, score):
        super().__init__(smartphone)
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

    def __str__(self):
        return (f'Smartphone {self.name} on {self.chip} with '
                f'{self.battery_capacity} tested on {self.date}')


def prepare_data():
    smartphones = Smartphones()
    smartphones.from_smartphone_bench_excel_book()
    smartphones = sorted(smartphones.all_smartphones,
                         key=lambda x: x.geek_bench4.total_score)

    y_axis_names = []
    x_axis_values = []
    x_axis_values2 = []

    for i, smartphone in enumerate(smartphones):
        # return name and chip of a smartphone with it index according to
        # its performance in GeekBench 4
        y_axis_names.append(f'{len(smartphones) - i}. {smartphone.name} '
                            f'({smartphone.chip})')
        x_axis_values.append(smartphone.geek_bench4.multi_core_score)
        x_axis_values2.append(smartphone.geek_bench4.single_core_score)

    return y_axis_names, x_axis_values, x_axis_values2


def main():
    smartphones = Smartphones()
    smartphones.from_smartphone_bench_excel_book()


if __name__ == '__main__':
    main()
