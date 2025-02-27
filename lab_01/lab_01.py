with open("input_1 (1).txt", "r") as file: 
    content = file.readlines()
    array1 = []
    array2 = []
    total_difference = 0
for line in content:
     num1, num2 = map(int, line.split())
     array1.append(num1)
     array2.append(num2)
sorted_array1 = sorted(array1)
sorted_array2 = sorted(array2)
total_difference = sum(abs(sorted_array1[i] - sorted_array2[i]) for i in range (len(sorted_array1)))
print("Загальна різниця:", total_difference)




