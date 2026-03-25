from structures.graph import Graph

class FriendManager:
    def __init__(self):
        self.graph = Graph()

    def create_user(self, name):
        self.graph.add_user(name)

    def add_friend(self, user1, user2):
        self.graph.add_friend(user1, user2)

    def show_friends(self, user):
        return self.graph.get_friends(user)

    def display(self):
        self.graph.display()
