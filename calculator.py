import argparse


def add(args):
    result = args.x + args.y
    print(result)


def subtract(args):
    result = args.x - args.y
    print(result)


def multiply(args):
    result = args.x * args.y
    print(result)


def divide(args):
    result = args.x / args.y
    print(result)


parser = argparse.ArgumentParser(description='A simple calculator')

subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
add_parser.add_argument('numbers', type=int, nargs='+')
add_parser.set_defaults(func=add)

subtract_parser = subparsers.add_parser('subtract')
subtract_parser.add_argument('numbers', type=int, nargs='+')
subtract_parser.set_defaults(func=subtract)

multiply_parser = subparsers.add_parser('multiply')
multiply_parser.add_argument('numbers', type=int, nargs='+')
multiply_parser.set_defaults(func=multiply)

divide_parser = subparsers.add_parser('divide')
divide_parser.add_argument('numbers', type=int, nargs='+')
divide_parser.set_defaults(func=divide)

args = parser.parse_args()
if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()
