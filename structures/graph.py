class Graph:
    def __init__(self):
        # adjacency list
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_friend(self, user1, user2):
        # avoid duplicates and ensure both users exist
        if user1 not in self.graph:
            self.add_user(user1)
        if user2 not in self.graph:
            self.add_user(user2)

        if user2 not in self.graph[user1]:
            self.graph[user1].append(user2)
        if user1 not in self.graph[user2]:
            self.graph[user2].append(user1)

    def remove_friend(self, user1, user2):
        if user1 in self.graph and user2 in self.graph[user1]:
            self.graph[user1].remove(user2)
        if user2 in self.graph and user1 in self.graph[user2]:
            self.graph[user2].remove(user1)

    def get_friends(self, user):
        return self.graph.get(user, [])

    def get_all_users(self):
        return list(self.graph.keys())

    def display(self):
        for user, friends in self.graph.items():
            print(f"{user} -> {friends}")
