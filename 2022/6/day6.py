import argparse
from os import path

__location__ = path.dirname(__file__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()


def part1(input):
    window_max = 4
    for line in input:
        seen = []
        for i in range(len(line)):
            if len(seen) == window_max:
                print("Window: " + str(seen) + " index " + str(i))
                break

            current_letter = line[i]
            if current_letter in seen:
                del seen[0 : seen.index(current_letter) + 1]

            seen.append(current_letter)


def part2(input):
    window_max = 14
    for line in input:
        seen = []
        for i in range(len(line)):
            if len(seen) == window_max:
                print("Window: " + str(seen) + " index " + str(i))
                break

            current_letter = line[i]
            if current_letter in seen:
                del seen[0 : seen.index(current_letter) + 1]

            seen.append(current_letter)


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2(input)
    else:
        print("Invalid input!")
