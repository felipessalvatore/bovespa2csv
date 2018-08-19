import argparse
try:
    from BovespaParser import BovespaParser
except ImportError:
    from bovespa2csv.BovespaParser import BovespaParser


def main():
    """
    Script to parse one txt file.
    """
    parser = argparse.ArgumentParser(description="Parse bovespa txt file to csv file or excel file") # noqa
    parser.add_argument('txt_path',
                        type=str, help='path to bovespa txt file')
    parser.add_argument('output_path',
                        type=str, help='path to simulate data to be saved')
    parser.add_argument("-e",
                        "--excel",
                        action="store_true",
                        default=False,
                        help="param to control if the script will parse to a csv or xlsx file (default=False -- csv)") # noqa

    args = parser.parse_args()
    msg = "not in the correct extension"
    parser = BovespaParser()
    if args.excel:
        assert args.output_path[-5:] == ".xlsx", msg
        parser.to_excel(args.txt_path, args.output_path)
    else:
        assert args.output_path[-4:] == ".csv", msg
        parser.to_csv(args.txt_path, args.output_path)


if __name__ == '__main__':
    main()
