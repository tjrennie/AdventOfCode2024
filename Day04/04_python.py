import numpy as np
import re

def read_input(fname):
    data = []
    with open(fname) as f:
        for line in f.readlines():
            data.append(str(line[:-1]))
    return data

def day04_part1(data):
    find = "XMAS"
    answer = 0
    
    # Horizontal
    for row in data:
        answer += len(re.findall("XMAS", row))
        answer += len(re.findall("SAMX", row))
    
    # Vertical
    for column in range(len(data[0])):
        col = ""
        for row in data:
            col += row[column]
        answer += len(re.findall("XMAS", col))
        answer += len(re.findall("SAMX", col))

    # Diagonal
    diagonals = []
    rows = len(data)
    cols = len(data[0])
    for d in range(rows + cols - 1):  # Total diagonals
        diagonal = []
        for r in range(rows):
            c = d - r  # Calculate the column index
            if 0 <= c < cols:  # Check if the column index is valid
                diagonal.append(data[r][c])
        diagonals.append(''.join(diagonal))
    for row in diagonals:
        answer += len(re.findall("XMAS", row))
        answer += len(re.findall("SAMX", row))

    # Diagonal
    diagonals = []
    rows = len(data)
    cols = len(data[0])
    for d in range(rows + cols - 1):  # Total diagonals
        diagonal = []
        for r in range(rows):
            c = d-r  # Calculate the column index
            if 0 <= c < cols:  # Check if the column index is valid
                diagonal.append(data[rows-r-1][c])
        diagonals.append(''.join(diagonal))
    for row in diagonals:
        answer += len(re.findall("XMAS", row))
        answer += len(re.findall("SAMX", row))
    
    print(answer)

def sense_cross(patch):
    diag1 = patch[0][0]+patch[1][1]+patch[2][2]
    diag2 = patch[2][0]+patch[1][1]+patch[0][2]
    diag1sense = (diag1=="MAS") or (diag1=="SAM")
    diag2sense = (diag2=="MAS") or (diag2=="SAM")
    return diag1sense and diag2sense

def day04_part2(data):
    rows = len(data)
    cols = len(data[0])
    ncross = 0
    for r in range(rows-2):
        for c in range(cols-2):
            patch = [
                data[c+0][r:r+3],
                data[c+1][r:r+3],
                data[c+2][r:r+3],
            ]
            cross = sense_cross(patch)
            if cross:
                ncross=ncross+1
    print(ncross)
    
if __name__=="__main__":
    data = read_input("Day04/04-1_input.txt")
    
    day04_part1(data)
    
    day04_part2(data)