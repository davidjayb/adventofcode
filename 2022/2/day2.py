import argparse
from os import path

__location__ = path.dirname(__file__)

opponent_rock = "A"
opponent_paper = "B"
opponent_scissors = "C"

play_rock = "X"
play_paper = "Y"
play_scissors = "Z"

score_rock = 1
score_paper = 2
score_scissors = 3

score_draw = 3
score_win = 6

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()


def part1(input):
    score = 0

    for line in input:
        opponent_play = line[0]
        my_play = line[2]

        cur_score = 0

        if opponent_play == opponent_rock:
            if my_play == play_rock:
                cur_score = score_rock + score_draw
            elif my_play == play_paper:
                cur_score = score_paper + score_win
            else:
                cur_score = score_scissors
        elif opponent_play == opponent_paper:
            if my_play == play_rock:
                cur_score = score_rock
            elif my_play == play_paper:
                cur_score = score_paper + score_draw
            else:
                cur_score = score_scissors + score_win
        elif opponent_play == opponent_scissors:
            if my_play == play_rock:
                cur_score = score_rock + score_win
            elif my_play == play_paper:
                cur_score = score_paper
            else:
                cur_score = score_scissors + score_draw

        score += cur_score

    print("Strategy given play " + str(score))


def part2(input):
    score = 0

    play_lose = play_rock
    play_draw = play_paper

    for line in input:
        opponent_play = line[0]
        my_play = line[2]

        cur_score = 0

        if opponent_play == opponent_rock:
            if my_play == play_lose:
                cur_score = score_scissors
            elif my_play == play_draw:
                cur_score = score_rock + score_draw
            else:
                cur_score = score_paper + score_win
        elif opponent_play == opponent_paper:
            if my_play == play_lose:
                cur_score = score_rock
            elif my_play == play_draw:
                cur_score = score_paper + score_draw
            else:
                cur_score = score_scissors + score_win
        elif opponent_play == opponent_scissors:
            if my_play == play_lose:
                cur_score = score_paper
            elif my_play == play_draw:
                cur_score = score_scissors + score_draw
            else:
                cur_score = score_rock + score_win

        score += cur_score

    print("Strategy given result " + str(score))


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2(input)
    else:
        print("Invalid input!")
