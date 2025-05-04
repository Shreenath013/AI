import heapq

def prim(graph, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        cost, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                heapq.heappush(min_heap, (graph[u][v], v))
                if cost != 0:
                    mst_edges.append((u, v, graph[u][v]))

    return mst_edges, total_cost

def get_graph(n):
    graph = [[0]*n for _ in range(n)]
    print("Enter weights between nodes (0 if no edge):")
    for i in range(n):
        for j in range(i+1, n):
            w = int(input(f"Weight between Node {i} and Node {j}: "))
            graph[i][j] = w
            graph[j][i] = w
    return graph

def main():
    n = int(input("Enter number of nodes: "))
    graph = get_graph(n)
    mst, cost = prim(graph, n)

    print("\nEdges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} (Weight: {w})")

    print(f"\nTotal cost of MST: {cost}")

main()
