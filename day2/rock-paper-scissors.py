item_score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

outcome_score = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6
}

opponent_letters = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

you_letters = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

with open("input.txt") as input:
    score = 0
    for line in input.readlines():
        opponent = opponent_letters[line[0]]
        you = you_letters[line[2]]
        if opponent == you:
            # Draw
            score += item_score[you] + outcome_score["Draw"]
        elif (opponent == "Rock" and you == "Scissors") or (opponent == "Scissors" and you == "Paper") or (opponent == "Paper" and you == "Rock"):
            # Lose
            score += item_score[you] + outcome_score["Lose"]
        else:
            # Win
            score += item_score[you] + outcome_score["Win"]
    print(score)