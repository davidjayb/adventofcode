import argparse
from itertools import islice
from os import path
from re import findall

__location__ = path.dirname(__file__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()

stack_1 = ["S", "L", "W"]
stack_2 = ["J", "T", "N", "Q"]
stack_3 = ["S", "C", "H", "F", "J"]
stack_4 = ["T", "R", "M", "W", "N", "G", "B"]
stack_5 = ["T", "R", "L", "S", "D", "H", "Q", "B"]
stack_6 = ["M", "J", "B", "V", "F", "H", "R", "L"]
stack_7 = ["D", "W", "R", "N", "J", "M"]
stack_8 = ["B", "Z", "T", "F", "H", "N", "D", "J"]
stack_9 = ["H", "L", "Q", "N", "B", "F", "T"]
stack_all = [
    None,
    stack_1,
    stack_2,
    stack_3,
    stack_4,
    stack_5,
    stack_6,
    stack_7,
    stack_8,
    stack_9,
]


def part1(input):
    for line in islice(input, 10, None):
        split_string = findall(r"\d+", line)
        num_to_move = int(split_string[0])
        move_from = int(split_string[1])
        move_to = int(split_string[2])

        for _ in range(num_to_move):
            stack_all[move_to].append(stack_all[move_from].pop())

    top_of_stacks = ""

    for stack in stack_all:
        if stack is not None:
            top_of_stacks += stack.pop()

    print(top_of_stacks)


def part2(input):
    for line in islice(input, 10, None):
        split_string = findall(r"\d+", line)
        num_to_move = int(split_string[0])
        move_from = int(split_string[1])
        move_to = int(split_string[2])

        stack_to_move_from = stack_all[move_from]
        stack_length = len(stack_to_move_from)
        elements_to_move = stack_to_move_from[stack_length - num_to_move : stack_length]
        stack_all[move_to].extend(elements_to_move)
        del stack_to_move_from[stack_length - num_to_move : stack_length]

    top_of_stacks = ""

    for stack in stack_all:
        if stack is not None:
            top_of_stacks += stack.pop()

    print(top_of_stacks)


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2(input)
    else:
        print("Invalid input!")
