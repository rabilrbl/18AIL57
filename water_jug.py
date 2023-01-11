# Water jug problem
from collections import defaultdict

visited = defaultdict(lambda: False)  # visited nodes
j1 = 5  # jug 1
j2 = 3  # jug 2
goal = 4  # goal to reach


def display(x, y):
    print(f"({x}, {y})")  # prints (x, y)


def solve(x, y):
    if x == goal and y == 0 or y == goal and x == 0:
        display(x, y)
        return True
    if not visited[(x, y)]:
        display(x, y)
        visited[(x, y)] = True
        return (
            solve(x, 0)
            or solve(0, y)
            or solve(j1, y)
            or solve(x, j2)
            or solve(x + min(y, j1 - x), y - min(y, j1 - x))
            or solve(x - min(x, j2 - y), y + min(x, j2 - y))
        )
    return False


# Run the program
print("Solution: ")
solve(0, 0)
