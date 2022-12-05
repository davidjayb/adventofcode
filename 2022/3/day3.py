import argparse
from os import path

__location__ = path.dirname(__file__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()


def part1(input):
    priority_sum = 0

    for line in input:
        compartment_one = line[: len(line) // 2]
        compartment_two = line[len(line) // 2 :]

        duplicates = list(set(compartment_one) & set(compartment_two))

        for duplicate in duplicates:
            if duplicate.isupper():
                priority_sum += ord(duplicate) - 38
            else:
                priority_sum += ord(duplicate) - 96

    print(priority_sum)


def part2(input):
    priority_sum = 0

    cur_group = []
    index = 0

    for line in input:
        index += 1
        cur_group.append(line.strip())
        if index % 3 == 0:
            badge = list(set(cur_group[0]) & set(cur_group[1]) & set(cur_group[2]))[0]
            if badge.isupper():
                priority_sum += ord(badge) - 38
            else:
                priority_sum += ord(badge) - 96
            cur_group.clear()

    print(priority_sum)


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2(input)
    else:
        print("Invalid input!")
