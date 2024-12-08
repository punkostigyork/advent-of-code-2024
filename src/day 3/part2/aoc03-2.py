import re


def sum_mul(file_path):
    mul_enabled = True
    total = 0

    with open(file_path, 'r') as file:
        memory = file.read()

    tokens = re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory)

    for token in tokens:
        match = token.group(0)

        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        elif match.startswith("mul"):
            if mul_enabled:
                x, y = map(int, re.findall(r"\d+", match))
                total += x * y

    return total


result = sum_mul('input.txt')
print(result)
