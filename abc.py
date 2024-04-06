graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

def bfs(start_node, target_node):
    visited = []
    queue = [[start_node]]

    if start_node == target_node:
        return [start_node]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            adjacent_nodes = graph[node]
            for neighbor in adjacent_nodes:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == target_node:
                    return new_path

            visited.append(node)

    return None

result = bfs('A', 'D')
if result:
    print("Path:", ' -> '.join(result))
else:
    print("No path found.")