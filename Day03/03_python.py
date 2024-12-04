import numpy as np
import re

def read_input(fname):
    data = ''
    with open(fname) as f:
        for line in f.readlines():
            data += str(line)
    return data

def day03_part1(data):
    results = re.findall(r"mul\((\d+),\s*(\d+)\)", data)
    answer = 0
    for _ in results:
        a, b = _
        answer += int(a) * int(b)
    print(answer)

def day03_part2(data):
    results = re.findall(r"(mul|do|don\'t)\((\d+,\d+|)\)", data)
    answer = 0
    active = True
    for _ in results:
        operation, args = _
        if operation != "mul":
            active = operation == "do"
            continue
        a, b = args.split(",")
        if active and (1 <= len(a) <= 3) and (1 <= len(b) <= 3):
            answer += int(a) * int(b)
    print(answer)
    
if __name__=="__main__":
    data = read_input("Day03/03-1_input.txt")
    
    day03_part1(data)
    
    day03_part2(data)