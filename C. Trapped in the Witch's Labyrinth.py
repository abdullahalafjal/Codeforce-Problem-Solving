from collections import defaultdict, deque

def solve_maze(t, test_cases):
    results = []

    def get_neighbors(x, y, n, m):
        """Return valid neighbors for the cell (x, y)."""
        neighbors = []
        if x > 0: neighbors.append((x - 1, y, 'U'))  # Up
        if x < n - 1: neighbors.append((x + 1, y, 'D'))  # Down
        if y > 0: neighbors.append((x, y - 1, 'L'))  # Left
        if y < m - 1: neighbors.append((x, y + 1, 'R'))  # Right
        return neighbors

    for n, m, grid in test_cases:
        graph = defaultdict(list)
        exits = set()

        # Build the graph and mark exits
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '?':
                    continue  # Leave unspecified cells for later
                neighbors = get_neighbors(i, j, n, m)
                for ni, nj, dir_ in neighbors:
                    if grid[i][j] == dir_:
                        graph[(i, j)].append((ni, nj))

        # Assign `?` directions optimally
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '?':
                    neighbors = get_neighbors(i, j, n, m)
                    for ni, nj, _ in neighbors:
                        graph[(i, j)].append((ni, nj))

        # Tarjan's Algorithm for SCC detection
        index = 0
        stack = []
        indices = {}
        lowlink = {}
        on_stack = set()
        sccs = []
        trapped_cells = set()

        def tarjan(v):
            nonlocal index
            indices[v] = index
            lowlink[v] = index
            index += 1
            stack.append(v)
            on_stack.add(v)

            for w in graph[v]:
                if w not in indices:
                    tarjan(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif w in on_stack:
                    lowlink[v] = min(lowlink[v], indices[w])

            # Root of an SCC
            if lowlink[v] == indices[v]:
                scc = []
                while stack:
                    node = stack.pop()
                    on_stack.remove(node)
                    scc.append(node)
                    if node == v:
                        break
                sccs.append(scc)

        for i in range(n):
            for j in range(m):
                if (i, j) not in indices:
                    tarjan((i, j))

        # Count trapped cells
        for scc in sccs:
            is_trapped = True
            for x, y in scc:
                neighbors = get_neighbors(x, y, n, m)
                for nx, ny, _ in neighbors:
                    if (nx, ny) not in graph:
                        is_trapped = False
                        break
                if not is_trapped:
                    break
            if is_trapped:
                trapped_cells.update(scc)

        results.append(len(trapped_cells))

    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    test_cases.append((n, m, grid))

# Solve and output results
results = solve_maze(t, test_cases)
print("\n".join(map(str, results)))
