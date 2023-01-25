# set current Elf to 1, total Calories for current Elf to 0, and maximum Calories seen so far to 0
current_elf = 1
total_calories = 0
max_calories = 0

# read the next line of input
input_file = open('input1.txt', 'r')
line = input_file.readline()

# while there is still input to process
while line:
    # if the line is blank, that means we have finished processing the current Elf's inventory
    # so we should update the maximum Calories seen so far if necessary and reset the total Calories for the current Elf
    if  line.strip() == "":
        max_calories = max(max_calories, total_calories)
        total_calories = 0
        current_elf = current_elf + 1
    # otherwise, we have a line with the Calories for one of the Elf's food items
    # so we add the Calories to the total for the current Elf
    else:
        total_calories = total_calories + int(line)
    # read the next line of input
    line = input_file.readline()

input_file.close()
# we have finished processing all of the input, so we need to update the maximum Calories seen so far one more time
max_calories = max(max_calories, total_calories)

# print the maximum Calories seen
print(max_calories)