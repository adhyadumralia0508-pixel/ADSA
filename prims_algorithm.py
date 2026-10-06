INF = float('inf')


def min_key(key, mst_set, vertices):
    minimum = INF
    min_index = -1

    for v in range(vertices):
        if not mst_set[v] and key[v] < minimum:
            minimum = key[v]
            min_index = v

    return min_index


def prim_mst(graph, vertices):
    parent = [-1] * vertices
    key = [INF] * vertices
    mst_set = [False] * vertices

    key[0] = 0

    for _ in range(vertices - 1):
        u = min_key(key, mst_set, vertices)

        mst_set[u] = True

        for v in range(vertices):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    print("\nEdge\tWeight")

    total_weight = 0

    for i in range(1, vertices):
        print(f"{parent[i]} - {i}\t{graph[i][parent[i]]}")
        total_weight += graph[i][parent[i]]

    print("Total Weight:", total_weight)


vertices = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(vertices):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph, vertices)
