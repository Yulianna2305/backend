with open("input.txt", "r") as file: 
    content = [list(map(int, line.split())) for line in file.readlines()]

def is_safe_report(report):
    increasing = decreasing = True
    
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False
    
    return increasing or decreasing

safe_reports = sum(is_safe_report(report) for report in content)

print(f"Кількість безпечних звітів: {safe_reports}")


