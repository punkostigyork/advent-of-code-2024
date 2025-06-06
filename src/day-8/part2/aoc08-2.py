def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def main():
    # Read the map
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
        if n < 2:
            continue
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                # Normalize direction for stepping
                g = gcd(dx, dy)
                step_x, step_y = dx // g, dy // g

                # Walk forwards from (x2, y2)
                x, y = x2, y2
                while True:
                    x += step_x
                    y += step_y
                    if in_bounds(x, y, width, height):
                        antinodes.add((x, y))
                    else:
                        break

                # Walk backwards from (x1, y1)
                x, y = x1, y1
                while True:
                    x -= step_x
                    y -= step_y
                    if in_bounds(x, y, width, height):
                        antinodes.add((x, y))
                    else:
                        break

                # Also, add all antennas of this frequency (they are on all lines for this freq)
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))

    print(len(antinodes))

if __name__ == "__main__":
    main()
