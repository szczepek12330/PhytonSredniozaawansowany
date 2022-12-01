import argparse
import configparser
import sys
import yaml

def main(number, other_number, output):
    result = number * other_number
    print(f'Wynik wynosi: {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help="Liczba", default=1)
    parser.add_argument('-n2', type=int, help="Inna liczba", default=1)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Plik konfiguracyjny w YAML', default=None)
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'),
                        help='Plik na dane wyjściowe', default=sys.stdout)

    args = parser.parse_args()
    if args.config:
        # config = configparser.ConfigParser()
        config = yaml.load(args.config, Loader=yaml.FullLoader)
        # config.read_file(args.config)
        # args.n1 = int(config['ARGUMENTS']['n1'])
        # args.n2 = int(config['ARGUMENTS']['n2'])
        args.n1 = config['ARGUMENTS']['n1']
        args.n2 = config['ARGUMENTS']['n2']

    main(args.n1, args.n2, args.output)

