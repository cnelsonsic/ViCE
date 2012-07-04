from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="ViCE's Command Line Interface")
    subparsers = parser.add_subparsers()

    create_parser = subparsers.add_parser('create',
        help='Create various plugins and their components.')
    create_parser.add_argument('rules',
        help='create a skeleton for a rules plugin')
    create_parser.add_argument('database',
        help='create a database')
    create_parser.add_argument('item',
        help='create a skeleton for an item plugin')
    create_parser.add_argument('action',
        help='create a skeleton for an action plugin')
    create_parser.add_argument('container',
        help='create a skeleton for an container plugin')
    create_parser.add_argument('--interactive', '-i',
        help='create component interactively')

    args = parser.parse_args()
    print args

if __name__ == '__main__':
    main()
