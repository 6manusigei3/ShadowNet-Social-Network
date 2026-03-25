from structures.heap import MaxHeap

def recommend_friends(graph, user):
    friends = set(graph.get_friends(user))
    recommendations = {}

    for friend in friends:
        for mutual in graph.get_friends(friend):
            if mutual != user and mutual not in friends:
                recommendations[mutual] = recommendations.get(mutual, 0) + 1

    heap = MaxHeap()

    for person, score in recommendations.items():
        heap.push(person, score)

    result = []

    while not heap.is_empty():
        result.append(heap.pop())

    return result
