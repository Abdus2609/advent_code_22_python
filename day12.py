def day12():
    with open("./input12.txt", "r") as file:
        grid = [[*line.strip()] for line in file.readlines()]

        # part 1
        queue = []
        for i, row in enumerate(grid):
            for j, pos in enumerate(row):
                if pos == 'S':
                    queue.insert(0, ((i, j), 0))

        print(search(grid, queue))

        # part 2
        queue_2 = []
        for i, row in enumerate(grid):
            for j, pos in enumerate(row):
                if height(pos) == 1:
                    queue_2.insert(0, ((i, j), 0))

        print(search(grid, queue_2))


def search(grid, queue):
    visited = set()
    while queue:
        (r, c), d = queue.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if grid[r][c] == 'E':
            return d
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r_new = r + dr
            c_new = c + dc
            if 0 <= r_new < len(grid) and 0 <= c_new < len(grid[0]) and height(grid[r_new][c_new]) <= 1 + height(
                    grid[r][c]):
                queue.insert(0, ((r_new, c_new), d + 1))


def height(c):
    if c == 'S':
        return 1
    elif c == 'E':
        return 26
    else:
        return ord(c) - ord('a') + 1


if __name__ == "__main__":
    day12()
