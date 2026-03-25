from system.friend_manager import FriendManager
from system.recommendation_engine import recommend_friends

fm = FriendManager()

fm.create_user("Alice")
fm.create_user("Bob")
fm.create_user("Carol")
fm.create_user("David")

fm.add_friend("Alice", "Bob")
fm.add_friend("Bob", "Carol")
fm.add_friend("Alice", "David")

fm.display()

print("Recommendations for Alice:")
print(recommend_friends(fm.graph, "Alice"))
