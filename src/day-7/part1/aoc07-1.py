import itertools

def evaluate_expression(numbers, ops):
    """Evaluate the numbers with ops (left-to-right, no precedence)."""
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def main():
    valid_test_values = []
    with open("input.txt", "r") as f:
        for line in f:
            if not line.strip():
                continue
            left, right = line.split(':')
            target = int(left.strip())
            numbers = list(map(int, right.strip().split()))
            num_ops = len(numbers) - 1
            for ops in itertools.product(['+', '*'], repeat=num_ops):
                if evaluate_expression(numbers, ops) == target:
                    valid_test_values.append(target)
                    break
    print(sum(valid_test_values))

if __name__ == "__main__":
    main()
