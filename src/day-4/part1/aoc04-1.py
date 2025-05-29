def find_xmas_in_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Function to check in all directions from a specific position
    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    # Check every possible position in the grid
    for r in range(rows):
        for c in range(cols):
            # Horizontal (right) and Horizontal (left)
            if check_direction(r, c, 0, 1):
                count += 1
            if check_direction(r, c, 0, -1):
                count += 1
            # Vertical (down) and Vertical (up)
            if check_direction(r, c, 1, 0):
                count += 1
            if check_direction(r, c, -1, 0):
                count += 1
            # Diagonal (down-right) and Diagonal (up-left)
            if check_direction(r, c, 1, 1):
                count += 1
            if check_direction(r, c, -1, -1):
                count += 1
            # Diagonal (down-left) and Diagonal (up-right)
            if check_direction(r, c, 1, -1):
                count += 1
            if check_direction(r, c, -1, 1):
                count += 1

    return count


def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines() if line.strip()]
    return grid


# Example usage
filename = 'input.txt'  # Replace with your file path
grid = read_grid_from_file(filename)

result = find_xmas_in_grid(grid)
print(f"XMAS appears {result} times.")
