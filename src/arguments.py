import argparse


def handle_arguments():
    parser = argparse.ArgumentParser(
        description="NeoMan - Beautiful & Powerfull man reader""")

    # Positional arguments
    parser.add_argument('command', metavar='command', type=str, nargs='+',
                        help='The command you want to read man')

    # Optional arguments
    """
    parser.add_argument('-s', dest='search',
                        help='Search a word or a pattern')

    
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    """

    return parser.parse_args()
