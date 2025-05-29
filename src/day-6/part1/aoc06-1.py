def simulate_guard_movement(grid):
    # Define direction vectors and rotation order
    directions = ['^', '>', 'v', '<']
    dir_vectors = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }

    # Find guard's starting position and direction
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                dir_index = directions.index(grid[r][c])
                break

    visited = set()
    r, c = guard_pos
    visited.add((r, c))

    while True:
        dr, dc = dir_vectors[directions[dir_index]]
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '#':
                dir_index = (dir_index + 1) % 4  # turn right
            else:
                r, c = nr, nc  # move forward
                visited.add((r, c))
        else:
            break  # guard leaves the map

    return len(visited)


def main():
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    count = simulate_guard_movement(grid)
    print("Visited positions:", count)


if __name__ == "__main__":
    main()
