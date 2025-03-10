with open("input.txt", "r") as file:
    content = file.readlines()
    
moves = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

results = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

points = {
    'Win': 3,
    'Draw': 1,
    'Lose': 0
}

total_score = 0

for line in content:
    move_code, result_code = line.strip().split()
    move = moves.get(move_code, '')  
    result = results.get(result_code, '') 
    if move and result:
        total_score += points[result]

print(f'Загальний рахунок: {total_score}')

