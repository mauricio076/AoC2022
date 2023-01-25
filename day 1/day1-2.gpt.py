# open the input file for reading
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input2.txt')
with open(filename, "r") as file:
  # set current Elf to 1, total Calories for current Elf to 0, and maximum Calories seen so far to 0
  current_elf = 1
  total_calories = 0
  max_calories = 0

  # create a list to store the top three Elves and their Calories
  top_elves = []

  # read each line in the file
  for line in file:
    # if the line is blank, that means we have finished processing the current Elf's inventory
    # so we should update the top three Elves if necessary and reset the total Calories for the current Elf
    if line.strip() == "":
      # if the current Elf's Calories are greater than the Calories for the least of the top three Elves,
      # we add the current Elf to the list
      if total_calories > min(top_elves, key=lambda x: x, default=0):
        top_elves.append(total_calories)
        # we only want to keep the top three Elves, so we remove the least of the top three Elves if necessary
        if len(top_elves) > 3:
          top_elves.remove(min(top_elves, key=lambda x: x))
      total_calories = 0
      current_elf = current_elf + 1
    # otherwise, we have a line with the Calories for one of the Elf's food items
    # so we add the Calories to the total for the current Elf
    else:
      total_calories = total_calories + int(line)

  # we have finished processing all of the input, so we need to update the top three Elves one more time
  if total_calories > min(top_elves, key=lambda x: x, default=0):
    top_elves.append( total_calories)
    if len(top_elves) > 3:
      top_elves.remove(min(top_elves, key=lambda x: x))

  # print the total Calories carried by the top three Elves
  print(sum(elf for elf in top_elves))
