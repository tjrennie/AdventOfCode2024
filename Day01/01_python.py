import numpy as np

def read_and_sort_input(fname):
    list1, list2 = np.loadtxt(fname, dtype=int).T
    list1 = np.sort(list1)
    list2 = np.sort(list2)
    return list1, list2

def day01_part1(list1,list2):
    answer = np.sum(np.abs(list1-list2))
    print(f"Part 1: {answer}")

def day01_part2(list1,list2):
    answer = sum(
        _ * sum(list2==_) for _ in list1
        )
    print(f"Part 2: {answer}")

if __name__ == "__main__":
    list1, list2 = read_and_sort_input("Day01/01-1_input.txt")
    day01_part1(list1, list2)
    day01_part2(list1, list2)