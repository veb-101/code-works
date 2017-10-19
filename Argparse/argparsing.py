#!usr/bin/python3


##import argparse
##parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,\
# help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int,\
# help="increase output verbosity", choices=[i for i in range(1,3)])
##args = parser.parse_args()
##answer = args.square**2
##
# if args.verbosity == 2:
##    print("the square of {} equals {}".format(args.square, answer))
# print(args.verbosity)
# elif args.verbosity == 1:
##    print("{}^2 == {}".format(args.square, answer))
# else:
# print(answer)
##

##import argparse
##parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
# help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count", default=0,
# help="increase output verbosity")
##args = parser.parse_args()
##answer = args.square**2
# if args.verbosity >= 2:
##    print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity >= 1:
##    print("{}^2 == {}".format(args.square, answer))
# else:
# print(answer)

import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
