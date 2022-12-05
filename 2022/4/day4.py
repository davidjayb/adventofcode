import argparse
from os import path

__location__ = path.dirname(__file__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()


def split_pairs(pairs):
    return pairs.split(",")


def split_assignment(assignment):
    return list(map(int, assignment.split("-")))


def part1(input):
    fully_contained_assignments = 0

    for line in input:
        elf_one, elf_two = split_pairs(line.strip())

        elf_one_assignment = split_assignment(elf_one)
        elf_two_assignment = split_assignment(elf_two)

        if (
            elf_one_assignment[0] >= elf_two_assignment[0]
            and elf_one_assignment[1] <= elf_two_assignment[1]
        ):
            fully_contained_assignments += 1
        elif (
            elf_one_assignment[0] <= elf_two_assignment[0]
            and elf_one_assignment[1] >= elf_two_assignment[1]
        ):
            fully_contained_assignments += 1

    print(fully_contained_assignments)


def part2(input):
    contained_assignments = 0

    for line in input:
        elf_one, elf_two = split_pairs(line.strip())

        elf_one_assignment = split_assignment(elf_one)
        elf_two_assignment = split_assignment(elf_two)

        if not (
            elf_one_assignment[0] > elf_two_assignment[1]
            or elf_one_assignment[1] < elf_two_assignment[0]
        ):
            contained_assignments += 1

    print(contained_assignments)


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2(input)
    else:
        print("Invalid input!")
