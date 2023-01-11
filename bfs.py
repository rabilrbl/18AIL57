from queue import PriorityQueue

graph = {
    0: [(1, 3), (2, 6), (3, 5)],
    1: [(4, 9), (5, 8)],
    2: [(6, 12), (7, 14)],
    3: [(8, 7)],
    8: [(9, 5), (10, 6)],
    9: [(11, 1), (12, 10), (13, 2)],
}


def bfs(start, target):
    visited = {
        node: False for node in graph.keys()
    }  # { 0: False, 1: False, 2: False, .... }
    pq = PriorityQueue()
    pq.put((0, start))
    visited[start] = True

    while not pq.empty():
        cost, node = pq.get()
        print("->", node, end=" ")

        if node == target:
            break

        for neighbor, cost in graph[node]:
            if not visited.get(neighbor):
                visited[neighbor] = True
                pq.put((cost, neighbor))

    print()  # for new line


bfs(0, 9)
