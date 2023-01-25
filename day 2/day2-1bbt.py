
score = 0

points = [
        [3,6,0,6,0],
        [0,3,6,0,3],
        [6,0,3,6,0],Temporal01i
        
        [0,6,0,3,6],
        [6,0,6,0,3]
    ];

# open the input file for reading
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input1.txt')
# open the input file for reading
with open(filename, "r") as file:
    for hand in file:
        if hand.strip() != "":
            items = hand.split()
            myHand = 0


            match items:
                case ['A', 'V']: # Rock - Rock (tied)
                    myHand = 3 + 1
                case ['A', 'W']: # Rock - Paper (win)
                   myHand = 6 + 2
                case ['A', 'X']:  # Rock - Scissors (losse)
                    myHand = 0 + 3
                case ['A', 'Y']:  # Rock - Lizzard (losse)
                    myHand = 0 + 4
                case ['A', 'Z']:  # Rock - Spock (win)
                    myHand = 6 + 5

                case ['B', 'X']: # Paper - Rock (losse)
                    myHand = 0 + 1
                case ['B', 'Y']: # Paper - Paper (tied)
                   myHand = 3 + 2
                case ['B', 'Z']:  # Paper - Scissors (win)
                    myHand = 6 + 3

                case ['C', 'X']: # Scissors - Rock (win)
                    myHand = 6 + 1
                case ['C', 'Y']: # Scissors - Paper (losse)
                   myHand = 0 + 2
                case ['C', 'Z']:  # Scissors - Scissors (tied)
                    myHand = 3 + 3       

            score += myHand


print(score)