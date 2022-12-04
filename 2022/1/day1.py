from os import path

__location__ = path.dirname(__file__)

with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    cur_calorie_count = 0
    elfs = []
    for line in input:
        if line != "\n":
            cur_calorie_count += int(line)
        else:
            elfs.append(cur_calorie_count)

            cur_calorie_count = 0

    elfs.sort(reverse=True)

    print("Most calories carried: " + str(elfs[0]))

    top_three_sum = elfs[0] + elfs[1] + elfs[2]
    print("Sum of top three carrieres: " + str(top_three_sum))

