import argparse
from os import path

__location__ = path.dirname(__file__)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-p", "--part", type=int)

args = arg_parser.parse_args()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name}"


class Dir:
    def __init__(self, name, parent_dir=None, dirs=None, files=None):
        self.name = name
        self.parent_dir = parent_dir
        if dirs is None:
            self.dirs = {}
        else:
            self.dirs = dirs

        if files is None:
            self.files = {}
        else:
            self.files = files

        self.size = 0

    def add_file(self, file_name, file_size):
        if file_name not in self.files:
            self.files.setdefault(file_name, File(file_name, file_size))
            self.size += file_size

    def calculate_size(self):
        size = 0

        for _, file in self.files.items():
            size += file.size

        for _, dir in self.dirs.items():
            size += dir.calculate_size()

        return size


def create_tree(input):
    root = Dir("/")
    current_node = root

    for line in input:
        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd "):
            go_to_dir = line.partition("$ cd ")[2].strip()
            if go_to_dir == "..":
                if not current_node.parent_dir:
                    continue
                current_node = current_node.parent_dir
            elif go_to_dir == "/":
                current_node = root
            else:
                current_node = current_node.dirs.get(
                    go_to_dir, Dir(go_to_dir, current_node)
                )
        elif line.startswith("dir "):
            sub_directory = line.partition(" ")[2].strip()
            current_node.dirs.setdefault(
                sub_directory, Dir(sub_directory, current_node)
            )
        else:
            file = line.partition(" ")
            file_size = file[0].strip()
            file_name = file[2].strip()
            current_node.add_file(file_name, int(file_size))

    return root


def calculate_dir_size(dir, max_size, sum):
    current_sum = dir.size

    for _, sub_directory in dir.dirs.items():
        sub_directory_sum = calculate_dir_size(sub_directory, max_size, sum)
        current_sum += sub_directory_sum

    if current_sum <= max_size:
        sum[0] += current_sum

    return current_sum


def part1(tree_root):
    max_size = 100000

    my_sum = [0]

    calculate_dir_size(tree_root, max_size, my_sum)

    print(my_sum[0])


def calculate_smallest_dir_size(dir, min_size, dir_to_delete):
    current_sum = dir.size

    for _, sub_directory in dir.dirs.items():
        sub_directory_sum = calculate_smallest_dir_size(
            sub_directory, min_size, dir_to_delete
        )
        current_sum += sub_directory_sum

    if current_sum >= min_size and current_sum <= dir_to_delete[0]:
        dir_to_delete[0] = current_sum

    return current_sum


def part2(tree_root):
    fs_size = 70000000
    space_required = 30000000

    tree_size = tree_root.calculate_size()
    minimum_space_to_free = space_required - (fs_size - tree_size)

    dir_to_delete = [tree_size]

    calculate_smallest_dir_size(tree_root, minimum_space_to_free, dir_to_delete)

    print(dir_to_delete[0])


with open(path.join(__location__, "input"), mode="r", encoding="utf-8") as input:
    tree_root = create_tree(input)
    if args.part == 1:
        part1(tree_root)
    elif args.part == 2:
        part2(tree_root)
    else:
        print("Invalid input!")
