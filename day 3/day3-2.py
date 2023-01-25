import os

dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, "input2.txt")


num = 3

def getPriority(item_type) -> int:
    priorities = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return priorities.index(item_type)

with open (filepath, "r") as file:
    sum = 0
    group = []
    for line in file:        
        group.append(set(line.strip()))
        if len(group) == num:
           common = set.intersection(*group)
           sum += getPriority(common.pop())
           group = []
    print(sum)