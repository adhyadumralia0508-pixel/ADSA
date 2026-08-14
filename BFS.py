MAX = 100

queue = [0] * MAX
front = -1
rear = -1
visited = [0] * MAX


def enqueue(vertex):
    global front, rear

    if rear == MAX - 1:
        return

    if front == -1:
        front = 0

    rear = rear + 1
    queue[rear] = vertex


def dequeue():
    global front, rear

    if front == -1:
        return -1

    vertex = queue[front]

    if front >= rear:
        front = -1
        rear = -1
    else:
        front = front + 1

    return vertex


def bfs(graph, startVertex, vertices):
    global visited

    for i in range(vertices):
        visited[i] = 0

    enqueue(startVertex)
    visited[startVertex] = 1

    print("BFS Traversal:", end=" ")

    while front != -1:
        currentVertex = dequeue()
        print(currentVertex, end=" ")

        for i in range(vertices):
            if graph[currentVertex][i] == 1 and visited[i] == 0:
                enqueue(i)
                visited[i] = 1


vertices = int(input("Enter number of vertices: "))

graph = [[0] * MAX for _ in range(MAX)]

print("Enter adjacency matrix:")

for i in range(vertices):
    for j in range(vertices):
        graph[i][j] = int(input())

startVertex = int(input("Enter starting vertex: "))

bfs(graph, startVertex, vertices)