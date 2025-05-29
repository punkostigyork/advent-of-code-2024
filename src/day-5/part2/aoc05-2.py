from collections import defaultdict, deque


def parse_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    split_index = next(i for i, line in enumerate(lines) if ',' in line)
    rules = [tuple(map(int, line.split('|'))) for line in lines[:split_index]]
    updates = [list(map(int, line.split(','))) for line in lines[split_index:]]

    return rules, updates


def is_update_valid(update, rules):
    pos = {val: i for i, val in enumerate(update)}
    for x, y in rules:
        if x in pos and y in pos and pos[x] > pos[y]:
            return False
    return True


def topological_sort(update, rules):
    # Restrict rules to this update
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]

    # Build graph
    adj = defaultdict(list)
    indegree = {u: 0 for u in update}
    for x, y in relevant_rules:
        adj[x].append(y)
        indegree[y] += 1

    # Kahn's algorithm
    queue = deque(sorted([u for u in update if indegree[u] == 0]))  # sorted to ensure stable output
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(update):
        raise ValueError("Cycle detected or incomplete sort")

    return result


def get_middle(lst):
    return lst[len(lst) // 2]


def main():
    rules, updates = parse_input("input.txt")
    total = 0

    for update in updates:
        if not is_update_valid(update, rules):
            sorted_update = topological_sort(update, rules)
            total += get_middle(sorted_update)

    print("Sum of middle pages from corrected updates:", total)


if __name__ == "__main__":
    main()
