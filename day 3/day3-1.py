import os

dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, "input1.txt")

priorities = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open (filepath, "r") as file:
    sum = 0
    for line in file:
        # find the lenght and split it on the middle
        linelen = len(line)
        center = int(linelen/2)
        first_compartment = set()
        second_compartment = set()
        for i in range(center):
            if line[i] == line[center+i]:
                sum += priorities.index(line[i])
                break
            elif first_compartment.issuperset({line[center+i]}):
                sum += priorities.index(line[center+i])
                break
            elif second_compartment.issuperset({line[i]}):
                sum += priorities.index(line[i])
                break
            else:       
                first_compartment.add(line[i])
                second_compartment.add(line[center+i])
    
    print(sum)