
score = 0
# open the input file for reading
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input2.txt')
# open the input file for reading
with open(filename, "r") as file:
    for hand in file:
        if hand.strip() != "":
            items = hand.split()
            myHand = 0
            theirHand = 0
            
            # Create my selection points
            match items[1]:
                case "X":
                    myHand = 1
                case "Y":
                    myHand = 2
                case "Z":
                    myHand = 3
                case _ :
                    myHand = 0


            match items:
                case ['A', 'X']: # Rock - Rock (tied)
                    myHand += 3
                case ['A', 'Y']: # Rock - Paper (win)
                   myHand += 6
                case ['A', 'Z']:  # Rock - Scissors (losse)
                    myHand += 0

                case ['B', 'X']: # Paper - Rock (losse)
                    myHand += 0
                case ['B', 'Y']: # Paper - Paper (tied)
                   myHand += 3
                case ['B', 'Z']:  # Paper - Scissors (win)
                    myHand += 6

                case ['C', 'X']: # Scissors - Rock (win)
                    myHand += 6
                case ['C', 'Y']: # Scissors - Paper (losse)
                   myHand += 0
                case ['C', 'Z']:  # Scissors - Scissors (tied)
                    myHand += 3       

            score += myHand

print(score)