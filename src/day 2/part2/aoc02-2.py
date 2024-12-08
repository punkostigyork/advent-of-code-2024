def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe(file_path):
    safe_count = 0
    with open(file_path, "r") as f:
        for line in f:
            report = list(map(int, line.strip().split()))
            if is_safe(report) or safe_with_dampener(report):
                safe_count += 1
    return safe_count


#-----------PART 2 SOLUTION------------

file_path = "input.txt"
result = count_safe(file_path)
print(result)
