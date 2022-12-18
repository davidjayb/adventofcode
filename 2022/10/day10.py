import argparse
from os import path
from math import floor

__location__ = path.dirname(__file__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()


def part1(input):
    current_cycle = 0
    current_x_value = 1

    signal_strength = 0

    for line in input:
        if line.startswith("addx"):
            current_cycle += 1

            if (current_cycle - 20) % 40 == 0:
                signal_strength += current_cycle * current_x_value

            current_cycle += 1
            x = int(line.partition(" ")[2].strip())
            current_x_value = current_x_value + x

            if (current_cycle - 20) % 40 == 0:
                signal_strength += current_cycle * (current_x_value - x)
        else:
            current_cycle += 1

            if (current_cycle - 20) % 40 == 0:
                signal_strength += current_cycle * current_x_value

    print(signal_strength)


def part2(input):
    pass


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2(input)
    else:
        print("Invalid input!")
