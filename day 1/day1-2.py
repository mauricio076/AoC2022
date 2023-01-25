# set current Elf to 1, total Calories for current Elf to 0, and maximum Calories seen so far to 0
current_elf = 1
total_calories = 0
max_calories = 0

# create a list to store the top three Elves and their Calories
top_elves = []

# read the next line of input
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input2.txt')
input_file = open(filename, 'r')

# while there is still input to process
for line in input_file:
    # if the line is blank, that means we have finished processing the current Elf's inventory
    # so we should update the top three Elves if necessary and reset the total Calories for the current Elf
    if line.strip() == "":

        if len(top_elves )< 3:
            top_elves.append( total_calories)
        else:
            min_elf = min(top_elves, key=lambda x: x, default=0)
            if total_calories > min_elf:
                top_elves.remove(min_elf)
                top_elves.append(total_calories)
        total_calories = 0
    else:
        total_calories = total_calories + int(line)

# we have finished processing all of the input, so we need to update the top three Elves one more time
max_calories = sum(top_elves)

input_file.close()
# print the total Calories carried by the top three Elves
print(max_calories)
