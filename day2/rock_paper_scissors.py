code_letters = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',  # +1
    'Y': 'Paper',  # +2
    'Z': 'Scissors'  # +3
}

code_results = {
    'X': 'Lose',  # +1
    'Y': 'Draw',  # +2
    'Z': 'Win'  # +3
}

decode_elements = []
shape_selected = 0
outcome = 0

with open("day2\source.txt", "r") as f:
    elements = [line.strip() for line in f]

for elem in elements:
    if elem == "A X":
        decode_elements.append("Rock Scissors")
    elif elem == "A Y":
        decode_elements.append("Rock Rock")
    elif elem == "A Z":
        decode_elements.append("Rock Paper")
    elif elem == "B X":
        decode_elements.append("Paper Rock")
    elif elem == "B Y":
        decode_elements.append("Paper Paper")
    elif elem == "B Z":
        decode_elements.append("Paper Scissors")
    elif elem == "C X":
        decode_elements.append("Scissors Paper")
    elif elem == "C Y":
        decode_elements.append("Scissors Scissors")
    elif elem == "C Z":
        decode_elements.append("Scissors Rock")


for elem in decode_elements:
    if elem == "Rock Rock" or elem == "Paper Paper" or elem == "Scissors Scissors":
        outcome += 3
    if elem == "Rock Paper" or elem == "Paper Scissors" or elem == "Scissors Rock":
        outcome += 6
    selected = elem.split(" ")[1]
    if selected == "Rock":
        shape_selected += 1
    else:
        if selected == "Paper":
            shape_selected += 2
        else:
            if selected == "Scissors":
                shape_selected += 3


# print(decode_elements)
print("*************************")
print(shape_selected)
print(outcome)
print(shape_selected + outcome)
