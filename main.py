from structures.graph import Graph

g = Graph()

g.add_user("Alice")
g.add_user("Bob")
g.add_user("Carol")

g.add_friend("Alice", "Bob")
g.add_friend("Bob", "Carol")

g.display()
