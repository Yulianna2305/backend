initial_stones = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]

def b_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
    for stone in stones:
        if stone == 0: 
            continue
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            split = len(str_stone) // 2
            new_stones.append(int(str_stone[:split]))
            new_stones.append(int(str_stone[split:]))
        else:
            new_stones.append(stone * 2024)

        stones = new_stones

    return stones
       
b_25 = b_stones(initial_stones, 25)
b_75 = b_stones(initial_stones, 75)

print (len(b_25)), (len(b_75))