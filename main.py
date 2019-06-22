# Main entry point to the app

from app_config import LIST_OF_BENCHS
from make_chart import make_chart
from prepare_data import Smartphones


def main() -> None:
    """
    Main entry point in the app.

    Runs all essential modules to read data
    and render charts

    :return: None
    """
    smartphones = Smartphones()
    smartphones.read_from_excel_book()

    # make a chart for every benchmark in a list
    for bench in LIST_OF_BENCHS:
        make_chart(bench, smartphones)


if __name__ == '__main__':
    main()
