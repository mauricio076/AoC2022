
score = 0
# open the input file for reading
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input1.txt')
# open the input file for reading
with open(filename, "r") as file:
    for hand in file:
        if hand.strip() != "":
            items = hand.split()
            match items:
                case ['A', 'X']: # Rock - losse (scissors)
                    myHand = 0 + 3
                case ['A', 'Y']: # Rock - draw (rock)
                   myHand = 3 + 1
                case ['A', 'Z']:  # Rock - win (paper)
                    myHand = 6 + 2 

                case ['B', 'X']: # Paper - Losse (rock)
                    myHand = 0 + 1
                case ['B', 'Y']: # Paper - draw (paper)
                   myHand = 3 + 2
                case ['B', 'Z']:  # Paper - win (scissors)
                    myHand = 6 + 3

                case ['C', 'X']: # Scissors - Losse (paper)
                    myHand = 0 + 2
                case ['C', 'Y']: # Scissors - draw (scissors)
                   myHand = 3 + 3
                case ['C', 'Z']:  # Scissors - win (rock)
                    myHand = 6 + 1       

            score += myHand

print(score)