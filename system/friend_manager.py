from structures.graph import Graph
from structures.stack import Stack

class FriendManager:
    def __init__(self):
        self.graph = Graph()
        self.history = Stack()

    def create_user(self, name):
        self.graph.add_user(name)

    def add_friend(self, user1, user2):
        self.graph.add_friend(user1, user2)
        self.history.push(("add", user1, user2))

    def remove_friend(self, user1, user2):
        self.graph.remove_friend(user1, user2)
        self.history.push(("remove", user1, user2))

    def undo(self):
        if self.history.is_empty():
            print("No actions to undo")
            return

        action, u1, u2 = self.history.pop()

        if action == "add":
            self.graph.remove_friend(u1, u2)
        elif action == "remove":
            self.graph.add_friend(u1, u2)

    def show_friends(self, user):
        return self.graph.get_friends(user)

    def display(self):
        self.graph.display()
