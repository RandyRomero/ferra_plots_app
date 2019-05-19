from datetime import datetime
import re
from dataclasses import dataclass
from typing import Optional, Dict, Tuple, Type

import openpyxl

from config import path_to_excel_workbook, the_last_row


class Benchmark:

    name: str = 'Benchmark name here'
    subtests: Tuple[str] = ()

    def __init__(self, smartphone):
        self.smartphone: Smartphone = smartphone

    def __str__(self):
        score_attrs = [getattr(self, attr) for attr in dir(self)
                       if 'score' in attr]

        response = (f'Smartphone {self.smartphone.name}, '
                    f'results in {__class__.name}:\n')
        response += f'Date: {self.smartphone.date}\n'

        for name, value in zip(GeekBench4.subtests, score_attrs):
            response += f'{name}: {value}\n'

        return response


class GeekBench4(Benchmark):

    name: str = 'GeekBench 4'
    subtests: Tuple[str] = ('Single-Core Score', 'Multi-Core Score',
                            'Total Score')

    def __init__(self, smartphone, multi_core_score, single_core_score):
        super().__init__(smartphone)

        self.multi_core_score: int = multi_core_score
        self.single_core_score: int = single_core_score
        self.total_score: int = multi_core_score + single_core_score


class Antutu7(Benchmark):

    name: str = 'AnTuTu Benchmark 7'
    subtests: Tuple[str] = ('Score',)

    def __init__(self, smartphone, score):
        super().__init__(smartphone)
        self.score = score


class SlingShotExtreme(Benchmark):
    """
    3DMark Sling Shot Extreme benchmark
    """

    name: str = '3DMark Sling Shot Extreme'
    subtests: Tuple[str] = ('Score',)

    def __init__(self, smartphone, score):
        super().__init__(smartphone)
        self.score = score


class BatteryTest(Benchmark):
    def __init__(self, smartphone, movie_score, read_score, game_score):
        super().__init__(smartphone)
        self.read_score = read_score
        self.movie_score = movie_score
        self.game_score = game_score
        self.total_score = movie_score + read_score + game_score


class Smartphones:
    def __init__(self):
        self.all_smartphones: Dict[str, Smartphone] = {}

    @staticmethod
    def _open_sheet(sheet_name):
        wb = openpyxl.load_workbook(path_to_excel_workbook)
        return wb[sheet_name]

    @staticmethod
    def _split_name(raw_name):
        regex = re.compile(r'^(.*)\((.*)\)')
        matches = re.search(regex, raw_name).groups()
        name, attr = matches[0].strip(), matches[1].strip()
        return name, attr

    def _make_table_reading_settings(self):

        @dataclass
        class TableReadingSettings:
            sheet_name: str
            table_start_row: int
            column_with_name: int
            columns_after_name: int
            bench_class: Type[Benchmark]
            bench_attr: str
            chip_or_capacity: str

            def return_variables(self):
                return (self.sheet_name,
                        self.table_start_row,
                        self.column_with_name,
                        self.columns_after_name,
                        self.bench_class,
                        self.bench_attr,
                        self.chip_or_capacity)

        geekbench4_trs = TableReadingSettings(sheet_name='GeekBench 4',
                                              table_start_row=12,
                                              column_with_name=32,
                                              columns_after_name=2,
                                              bench_class=GeekBench4,
                                              bench_attr='geek_bench4',
                                              chip_or_capacity='chip')

        sling_shot_extreme_trs = TableReadingSettings(
            sheet_name='3DMark Sling Shot Extreme',
            table_start_row=5,
            column_with_name=29,
            columns_after_name=1,
            bench_class=SlingShotExtreme,
            bench_attr='sling_shot_extreme',
            chip_or_capacity='chip')

        antutu7_trs = TableReadingSettings(sheet_name='Antutu Benchmark 7',
                                           table_start_row=3,
                                           column_with_name=29,
                                           columns_after_name=1,
                                           bench_class=Antutu7,
                                           bench_attr='antutu7',
                                           chip_or_capacity='chip')

        battery_test_trs = TableReadingSettings(sheet_name='battery_test',
                                                table_start_row=4,
                                                column_with_name=34,
                                                columns_after_name=3,
                                                bench_class=BatteryTest,
                                                bench_attr='battery_test',
                                                chip_or_capacity=
                                                'battery_capacity')

        trs = {'geek_bench4': geekbench4_trs,
               'sling_shot': sling_shot_extreme_trs,
               'antutu7': antutu7_trs,
               'battery_test': battery_test_trs}

        return trs

    def _from_benchmark_table(self, table_reading_settings):

        # Get different setting for different benchmarks
        sheet_name, table_start_row, column_with_name, columns_after_name, \
         bench_class, bench_attr, \
         chip_or_capacity = table_reading_settings.return_variables()

        # where my table with results of smartphones begins
        sheet = self._open_sheet(sheet_name)
        for row in range(table_start_row, the_last_row, 1):
            raw_name = sheet.cell(row=row, column=column_with_name).value

            # means that script has reached the end of the list with results
            if not raw_name:
                print('\nDone working on GeekBench 4 table\n')
                return

            # split name from an additional characteristic in parentheses
            name, characteristic = self._split_name(raw_name)

            # get a smartphone object from the dict or create new one
            if name not in self.all_smartphones.keys():
                smartphone = Smartphone(name)
                self.all_smartphones[name] = smartphone
                print(f'ADD {name} from {sheet_name}')
            else:
                smartphone = self.all_smartphones[name]
                print(f'UPDATE {name} from {sheet_name}')

            # set chip or battery capacity value to a smartphone object
            setattr(smartphone, chip_or_capacity, characteristic)

            # set date if it hasn't been done yet and if it is possible
            if not smartphone.date:
                raw_date = sheet.cell(row=row,
                                      column=column_with_name - 1).value
                if raw_date:
                    smartphone.date = raw_date.date()

            # gather results of a benchmark
            results = []
            for i in range(1, columns_after_name + 1, 1):
                result = sheet.cell(row=row, column=column_with_name + i).value
                results.append(result)

            bench = bench_class(smartphone, *results)
            setattr(smartphone, bench_attr, bench)

    def read_from_excel_book(self):
        """
        Making a list of smartphones by reading Excel sheets with certain data
        :return: None
        """
        trs = self._make_table_reading_settings()
        for test in ('geek_bench4', 'sling_shot', 'antutu7', 'battery_test'):
            self._from_benchmark_table(trs[test])


@dataclass
class Smartphone:
    name: str
    date: Optional[datetime] = None
    chip: Optional[str] = None
    battery_capacity: Optional[str] = None
    geek_bench4: Optional[GeekBench4] = None
    sling_shot_extreme: Optional[SlingShotExtreme] = None
    antutu7: Optional[Antutu7] = None
    battery_test: Optional[BatteryTest] = None

    def __str__(self):
        return (f'Smartphone {self.name} on {self.chip} with '
                f'{self.battery_capacity} tested on {self.date}')


def prepare_data():
    smartphones = Smartphones()
    smartphones.read_from_excel_book()
    smartphones_list = [x for x in smartphones.all_smartphones.values()
                        if x.geek_bench4]
    smartphones = sorted(smartphones_list,
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
    smartphones.read_from_excel_book()


if __name__ == '__main__':
    main()
