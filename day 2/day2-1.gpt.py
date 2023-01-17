def calculate_score(strategy_guide: str) -> int:
    score = 0
    for round in strategy_guide.split():
        opponent_choice = round[0]
        your_choice = round[1]

        if opponent_choice == your_choice:
            score += 3
        elif (opponent_choice == "A" and your_choice == "Y") or (opponent_choice == "B" and your_choice == "X") or (opponent_choice == "C" and your_choice == "Z"):
            score += 6
        else:
            score += 0
    return score

theScore = 0

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input2.txt')
# open the input file for reading
with open(filename, "r") as file:
    for hand in file:
        if hand.strip() != "":
           theScore += calculate_score(hand) 