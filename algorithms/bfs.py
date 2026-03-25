from structures.queue import Queue

def bfs(graph, start):
    visited = set()
    q = Queue()

    visited.add(start)
    q.enqueue(start)

    result = []

    while not q.is_empty():
        node = q.dequeue()
        result.append(node)

        for neighbor in graph.get_friends(node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.enqueue(neighbor)

    return result
