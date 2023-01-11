from itertools import permutations


def tsp(graph):
    size = len(graph)
    costs = []
    for path in permutations(range(1, size)):
        cost = graph[0][path[0]]
        for i in range(1, size - 1):
            cost += graph[path[i - 1]][path[i]]
        cost += graph[path[-1]][0]
        costs.append(cost)
    return min(costs)


graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print("Total cost:", tsp(graph))
