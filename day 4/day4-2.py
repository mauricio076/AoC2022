import os

dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, "input2.txt")

with open(filepath, "r") as file:
    acc = 0
    for line in file:
       
        # spliting line into an array, first half is elf1 and second half is elf2
        elfs = line.strip().replace(',','-').split('-')
        if int(elfs[1]) >= int(elfs[2]) and int(elfs[3]) >= int(elfs[0]):
            acc += 1
    print(acc)
