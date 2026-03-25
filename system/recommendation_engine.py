def recommend_friends(graph, user):
    friends = set(graph.get_friends(user))
    recommendations = {}

    for friend in friends:
        for mutual in graph.get_friends(friend):
            if mutual != user and mutual not in friends:
                if mutual not in recommendations:
                    recommendations[mutual] = 0
                recommendations[mutual] += 1

    # sort by number of mutual friends
    sorted_recommendations = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_recommendations
