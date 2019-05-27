from config import list_of_benchs
from make_chart import make_chart
from prepare_data import Smartphones

# todo make it accept command line arguments
# todo make names of highlighted smarphones bold with <b></b>


def main():
    smartphones = Smartphones()
    smartphones.read_from_excel_book()

    for bench in list_of_benchs:
        make_chart(bench, smartphones)


if __name__ == '__main__':
    main()
