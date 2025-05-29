def read_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f if line.strip()]

def find_guard(grid):
    directions = ['^', '>', 'v', '<']
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in directions:
                return (r, c), directions.index(grid[r][c])
    raise ValueError("Guard not found")

def simulate(grid, start_pos, start_dir, extra_block=None):
    # Direction vectors: up, right, down, left
    directions = ['^', '>', 'v', '<']
    dir_vecs = [(-1,0), (0,1), (1,0), (0,-1)]

    rows, cols = len(grid), len(grid[0])
    visited_states = set()

    r, c = start_pos
    d = start_dir

    while True:
        if ((r, c), d) in visited_states:
            return True  # loop detected
        visited_states.add(((r, c), d))

        dr, dc = dir_vecs[d]
        nr, nc = r + dr, c + dc

        # Check bounds
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False  # exits the grid

        # Check obstacle (including temporary one)
        if grid[nr][nc] == '#' or (extra_block == (nr, nc)):
            d = (d + 1) % 4  # turn right
        else:
            r, c = nr, nc  # move forward

def count_loop_obstruction_positions(grid):
    start_pos, start_dir = find_guard(grid)
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) == start_pos:
                continue
            if grid[r][c] != '.':
                continue
            if simulate(grid, start_pos, start_dir, extra_block=(r, c)):
                count += 1

    return count

if __name__ == "__main__":
    grid = read_input("input.txt")
    result = count_loop_obstruction_positions(grid)
    print("Number of positions that cause a loop:", result)
