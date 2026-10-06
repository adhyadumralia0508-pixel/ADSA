INF = float('inf')

n = int(input("Enter number of vertices: "))

graph = []

print("Enter the adjacency matrix:")
print("Enter INF for no direct path")

for i in range(n):
    row = []
    for j in range(n):
        value = input(f"graph[{i}][{j}]: ")

        if value.upper() == "INF":
            row.append(INF)
        else:
            row.append(int(value))

    graph.append(row)

dist = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        dist[i][j] = graph[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (dist[i][k] != INF and
                    dist[k][j] != INF and
                    dist[i][k] + dist[k][j] < dist[i][j]):

                dist[i][j] = dist[i][k] + dist[k][j]

print("\nShortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print("INF", end="\t")
        else:
            print(dist[i][j], end="\t")
    print()
