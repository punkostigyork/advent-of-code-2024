def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            tl = grid[i - 1][j - 1]
            tr = grid[i - 1][j + 1]
            c  = grid[i][j]
            bl = grid[i + 1][j - 1]
            br = grid[i + 1][j + 1]

            diag1 = tl + c + br
            diag2 = tr + c + bl

            if diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}:
                count += 1

    return count

# Read from file
def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

# Example usage
if __name__ == "__main__":
    filename = "input.txt"  # Make sure this file exists
    grid = read_grid_from_file(filename)
    print("X-MAS count:", count_xmas(grid))
