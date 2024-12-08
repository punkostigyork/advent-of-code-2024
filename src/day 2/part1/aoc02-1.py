def inc(numbers):
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))

def dec(numbers):
    return all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

safe = 0

with open("input.txt", 'r') as f:
    for line in f:
        numbers = list(map(int, line.split()))

        if not (inc(numbers) or dec(numbers)):
            continue

        for i in range(len(numbers) - 1):
            if abs(numbers[i] - numbers[i + 1]) > 3:
                break
        else:
            safe += 1

print(safe)
