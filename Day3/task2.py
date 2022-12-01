import argparse
import configparser
import sys
from datetime import datetime
import logging

LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG


def main(number, other_number, output):
    logging.info(f'Dzielenie {number} przez {other_number}')
    result = number / other_number
    print(f'[{datetime.now().isoformat()}] Wynik wynosi: {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', type=int, help="Liczba", default=1)
    parser.add_argument('-n2', type=int, help="Inna liczba", default=1)
    # parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Plik konfiguracyjny', default='automate.ini')
    parser.add_argument('-o', dest='output', type=argparse.FileType('a'), help='Plik na dane wyjściowe',
                        default=sys.stdout)
    parser.add_argument('-l', dest='log', type=str, help='Plik dziennika', default=None)

    args = parser.parse_args()
    if args.log:
        logging.basicConfig(format=LOG_FORMAT, filename=args.log, level=LOG_LEVEL)
    else:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
    try:
        main(args.n1, args.n2, args.output)
    except Exception as e:
        logging.exception("Bła w czasie wykonania zadania")
        exit(1)

    # if args.config:
    #     config = configparser.ConfigParser()
    #     config.read_file(args.config)
    #     args.n1 = int(config['ARGUMENTS']['n1'])
    #     args.n2 = int(config['ARGUMENTS']['n2'])
