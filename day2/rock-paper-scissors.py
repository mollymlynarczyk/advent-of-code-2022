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

outcome_letters = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

pick = {
    "Draw": {
        "Scissors": "Scissors",
        "Rock": "Rock",
        "Paper": "Paper"
    },
    "Win" : {
        "Rock": "Paper",
        "Scissors": "Rock",
        "Paper": "Scissors"
    },
    "Lose": {
        "Paper": "Rock",
        "Rock": "Scissors",
        "Scissors": "Paper"
    }
}

with open("input.txt") as input:
    score = 0
    for line in input.readlines():
        opponent = opponent_letters[line[0]]
        outcome = outcome_letters[line[2]]
        you = pick[outcome][opponent]
        score += item_score[you] + outcome_score[outcome]
    print(score)