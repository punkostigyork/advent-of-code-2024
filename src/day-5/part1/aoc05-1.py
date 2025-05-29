def parse_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    split_index = next(i for i, line in enumerate(lines) if ',' in line)
    rules = [tuple(map(int, line.split('|'))) for line in lines[:split_index]]
    updates = [list(map(int, line.split(','))) for line in lines[split_index:]]

    return rules, updates


def is_update_valid(update, rules):
    position = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in position and y in position:
            if position[x] > position[y]:
                return False
    return True


def get_middle(lst):
    return lst[len(lst) // 2]


def main():
    rules, updates = parse_input("input.txt")
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            total += get_middle(update)
    print("Sum of middle pages:", total)


if __name__ == "__main__":
    main()
