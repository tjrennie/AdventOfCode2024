import numpy as np

def read_input(fname):
    data = []
    with open(fname) as f:
        for line in f.readlines():
            line_s = line.split("\n")[0].split(" ")
            line_parsed = np.array([int(_) for _ in line_s])
            data.append(line_parsed)
    return data

def day02_part1(data):
    n_safe = 0
    for line in data:
        diffs = line[1:] - line[:-1]
        safe_diff = np.all(np.all([
            np.abs(diffs)>=1,
            np.abs(diffs)<=3,
        ], axis=0), axis=-1)
        safe_trend = np.all([
            np.any(diffs>0),
            np.any(diffs<0)], axis=0)==False
        safe = np.all([safe_diff, safe_trend], axis=0)
        if safe:
            n_safe += 1
    print(n_safe)

def test_safe(line):
    diffs = line[1:] - line[:-1]
    safe_diff = np.all(np.all([
        np.abs(diffs)>=1,
        np.abs(diffs)<=3,
    ], axis=0), axis=-1)
    safe_trend = np.all([
        np.any(diffs>0),
        np.any(diffs<0)], axis=0)==False
    safe = np.all([safe_diff, safe_trend], axis=0)
    return safe

def day02_part2(data):
    n_safe = 0
    for line in data:
        safe_all = test_safe(line)
        if safe_all:
            n_safe += 1
        else:
            for _ in range(line.shape[0]):
                mask = np.ones(line.shape, dtype=bool)
                mask[_] = False
                safe = test_safe(line[mask])
                if safe:
                    n_safe += 1
                    break
    print(n_safe)
    
if __name__=="__main__":
    data = read_input("Day02/02-1_input.txt")
    
    # day02_part1(data)
    
    day02_part2(data)