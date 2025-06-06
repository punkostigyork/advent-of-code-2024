def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def main():
    # Read map from file
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    height = len(lines)
    width = len(lines[0])

    # Map frequency -> list of (x, y) tuples
    antennas = {}
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != '.':
                antennas.setdefault(c, []).append((x, y))

    antinodes = set()
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                # Antinode beyond x2,y2
                ax, ay = x2 + dx, y2 + dy
                if in_bounds(ax, ay, width, height):
                    antinodes.add((ax, ay))
                # Antinode beyond x1,y1
                bx, by = x1 - dx, y1 - dy
                if in_bounds(bx, by, width, height):
                    antinodes.add((bx, by))

    # Count all unique antinode locations
    print(len(antinodes))

if __name__ == "__main__":
    main()
