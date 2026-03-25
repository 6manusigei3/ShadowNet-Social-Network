def sort_recommendations(data):
    return sorted(data, key=lambda x: x[1], reverse=True)
