import numpy as np
import itertools
from tqdm import tqdm
from collections import defaultdict, deque

def read_input(fname):
    ordering = []
    data = []
    with open(fname) as f:
        type = 0
        for line in f.readlines():
            if line.strip() == "":
                type = 1
            elif type == 0:
                ordering.append(np.array(line[:-1].split("|")).astype(int))
            elif type == 1:
                data.append(np.array(line[:-1].split(",")).astype(int))
    ordering = np.array(ordering)
    return ordering, data

def day05_part1(ordering, data):
    sum_middle = 0
    for pages in data:
        correct = True
        for rule in ordering:
            if (rule[0] in pages) and (rule[1] in pages):
                i_1 = np.where(rule[0]==pages)
                i_2 = np.where(rule[1]==pages)
                if i_1 >= i_2:
                    correct=False
        if correct:
            npages = pages.shape[0]
            sum_middle += pages[npages//2]
    print(sum_middle)

def reorder_list(first_list, pairs):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for num in first_list:
        in_degree[num] = 0
    
    for a, b in pairs:
        if a in in_degree and b in in_degree:
            graph[a].append(b)
            in_degree[b] += 1
    
    queue = deque([num for num in first_list if in_degree[num] == 0])
    ordered_list = []
    
    while queue:
        current = queue.popleft()
        ordered_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    unordered_elements = [num for num in first_list if num not in ordered_list]
    ordered_list.extend(unordered_elements)
    
    return ordered_list
    
def day05_part2(ordering, data):
    sum_middle = 0
    for pages in tqdm(data):
        correct = True
        for rule in ordering:
            if (rule[0] in pages) and (rule[1] in pages):
                i_1 = np.where(rule[0]==pages)
                i_2 = np.where(rule[1]==pages)
                if i_1 >= i_2:
                    correct=False
        if not correct:
            ordered = np.array(reorder_list(pages, ordering))
            npages = ordered.shape[0]
            sum_middle += ordered[npages//2]
    print(sum_middle)
    
if __name__=="__main__":
    ordering,data = read_input("Day05/05-1_input.txt")
    
    day05_part1(ordering, data)
    
    day05_part2(ordering, data)