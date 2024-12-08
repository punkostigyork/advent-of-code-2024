import re


def sum_of_mul(file_path):
    with open(file_path, "r") as file:
        memory = file.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total

result = sum_of_mul('input.txt')
print(result)
