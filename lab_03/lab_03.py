with open("input.txt", "r") as file:
    content = file.readlines()

def extract_number(line):
    digits = [char for char in line if char.isdigit()] 
    if digits: 
        return int(digits[0] + digits[-1])  
    return 0

total_sum = sum(extract_number(line) for line in content) 

print("Сума всіх калібрувальних значень:", total_sum)
    