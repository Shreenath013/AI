import queue

# Graph represented as an adjacency matrix
graph = [
    [0, 1, 1, 1, 0],  # A
    [1, 0, 1, 1, 1],  # B
    [1, 1, 0, 1, 0],  # C
    [1, 1, 1, 0, 1],  # D
    [0, 1, 0, 1, 1]   # E
]

# Node labels
nodes = ['A', 'B', 'C', 'D', 'E']

# Helper function to get index of a node
def get_index(node_label):
    return nodes.index(node_label)

# BFS traversal function
def bfs(start_index):
    visited = [False] * len(nodes)
    result = []
    q = queue.Queue()

    visited[start_index] = True
    q.put(start_index)

    while not q.empty():
        current = q.get()
        result.append(nodes[current])

        for neighbor in range(len(nodes)):
            if graph[current][neighbor] == 1 and not visited[neighbor]:
                q.put(neighbor)
                visited[neighbor] = True

    return result

# DFS traversal function
def dfs(start_index):
    visited = [False] * len(nodes)
    result = []
    stack = [start_index]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(nodes[current])

            # Push neighbors in reverse order for proper traversal
            for neighbor in reversed(range(len(nodes))):
                if graph[current][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return result

# Start from node 'E' (index 4)
start_node_index = 4

bfs_result = bfs(start_node_index)
dfs_result = dfs(start_node_index)

print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)
