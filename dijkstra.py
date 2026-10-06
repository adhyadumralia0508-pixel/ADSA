INF = float('inf')


def dijkstra(graph, source, n):
    distance = [INF] * n
    visited = [False] * n

    distance[source] = 0

    for count in range(n):
        u = -1

        for i in range(n):
            if not visited[i] and (u == -1 or distance[i] < distance[u]):
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if (not visited[v] and
                    graph[u][v] != 0 and
                    distance[u] + graph[u][v] < distance[v]):

                distance[v] = distance[u] + graph[u][v]

    return distance


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex: "))

distance = dijkstra(graph, source, n)

print("Shortest distances from source vertex", source, ":")

for i in range(n):
    if distance[i] == INF:
        print("Vertex", i, ": INF")
    else:
        print("Vertex", i, ":", distance[i])
