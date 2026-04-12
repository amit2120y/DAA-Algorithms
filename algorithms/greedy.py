def fractional_knapsack(weights, values, capacity):
    # 1. Calculate Profit-Weight Ratio for each item
    n = len(values)
    ratio = []
    for i in range(n):
        ratio.append((values[i] / weights[i], weights[i], values[i]))

    # 2. Sort items in descending order based on the ratio
    # x[0] refers to the ratio (profit/weight)
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0.0
    
    # 3. Iterate through sorted items to fill the knapsack
    for r, w, p in ratio:
        if capacity >= w:
            # Add the whole item if capacity allows
            capacity -= w
            total_profit += p
        else:
            # Add a fraction of the item if capacity is limited
            total_profit += p * (capacity / w)
            break  # Knapsack is full
            
    return total_profit

def kruskal_algorithm(n, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree - O(E log E)
    
    Greedy approach: Sort edges by weight, add edges without creating cycles.
    Uses Union-Find (Disjoint Set Union) to efficiently detect cycles.
    
    Args:
        n: Number of vertices
        edges: List of tuples (vertex1, vertex2, weight)
    
    Returns:
        mst: List of edges in the minimum spanning tree
        total_weight: Total weight of the MST
    """
    
    class UnionFind:
        """Data structure to efficiently detect cycles (connected components)"""
        def __init__(self, n):
            self.parent = list(range(n))  # Each vertex is its own parent initially
            self.rank = [0] * n  # Track tree depth for optimization
        
        def find(self, x):
            """Find the root/representative of vertex x's component"""
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]
        
        def union(self, x, y):
            """
            Union two components. Returns True if successful (no cycle),
            False if they're already in the same component (would create cycle)
            """
            root_x = self.find(x)
            root_y = self.find(y)
            
            # Already in same component → would create a cycle
            if root_x == root_y:
                return False
            
            # Union by rank: attach smaller tree under larger tree
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            return True
    
    # Step 1: Sort all edges by weight (ascending)
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize Union-Find data structure
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    # Step 3: Greedily add edges if they don't create cycles
    for u, v, w in edges_sorted:
        # Try to union the two components
        if uf.union(u, v):
            # Edge added successfully (no cycle created)
            mst.append((u, v, w))
            total_weight += w
            
            # MST always has exactly (V - 1) edges
            if len(mst) == n - 1:
                break
    
    return mst, total_weight

def prim_algorithm(n, edges):
    """Prim's Algorithm for Minimum Spanning Tree - O(E log V)"""
    import heapq
    
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    visited = [False] * n
    mst = []
    total_weight = 0
    heap = [(0, 0, -1)]  # (weight, node, parent)
    
    while heap:
        w, u, parent = heapq.heappop(heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, w))
            total_weight += w
        
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v, u))
    
    return mst, total_weight

def optimal_merge_pattern(file_sizes):
    """Optimal Merge Pattern - O(n log n)"""
    import heapq
    
    if not file_sizes:
        return 0
    
    heap = file_sizes[:]
    heapq.heapify(heap)
    total_cost = 0
    merges = []
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        merged = first + second
        total_cost += merged
        merges.append((first, second, merged))
        heapq.heappush(heap, merged)
    
    return total_cost, merges