class Graph:
    def __init__(self, graph, heuristicNode, startNode):
        self.graph = graph
        self.H = heuristicNode
        self.start = startNode
        self.solution = {}

    def getNext(self, v):
        # Find neighbors of node v
        return self.graph.get(v, "")  # if v is not in graph then gives ""

    def getHeuristicNode(self, n):
        return self.H.get(n, 0)  # if n is not in heuristic then gives 0

    def computeMinCost(self, v):
        minCost = 0
        costToChild = {}
        costToChild[minCost] = []
        flag = True
        for node in self.getNext(v):
            cost = 0
            nodeList = []
            for c, weight in node:
                print(f"Processing {c}")
                cost += self.getHeuristicNode(c) + weight
                nodeList.append(c)
            if flag or cost < minCost:
                minCost = cost
                costToChild[minCost] = nodeList
                flag = False
        return minCost, costToChild[minCost]

    def aoStar(self, v):
        minCost, childNodeList = self.computeMinCost(v)
        print(f"Node: {v}  Min Cost: {minCost}  Child Nodes: {childNodeList}")
        self.solution[v] = childNodeList
        print(f"Solution: {self.solution}")
        print("-" * 50) # for better visualization, you can skip this line
        for childNode in childNodeList:
            self.aoStar(childNode)


# for simplicity, we'll consider heuristic distances given
heuristic = {
    "A": 1,
    "B": 6,
    "C": 12,
    "D": 10,
    "E": 4,
    "F": 4,
    "G": 5,
    "H": 7,
}  # Heuristic values of Nodes

graph = {  # Graph of Nodes and Edges
    "A": [
        [("B", 1), ("C", 1)],
        [("D", 1)],
    ],  # Neighbors of Node 'A', B, C & D with repective weights
    "B": [[("G", 1)], [("H", 1)]],  # Neighbors are included in a list of lists
    "D": [[("E", 1), ("F", 1)]],  # Each sublist indicate a "OR" node or "AND" nodes
}

g = Graph(graph, heuristic, "A")
g.aoStar("A")

print("Graph Solution:")
print(g.solution)
