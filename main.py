from system.friend_manager import FriendManager
from system.recommendation_engine import recommend_friends

fm = FriendManager()

# Create users
fm.create_user("Alice")
fm.create_user("Bob")
fm.create_user("Carol")
fm.create_user("David")

# Add friendships
fm.add_friend("Alice", "Bob")
fm.add_friend("Bob", "Carol")
fm.add_friend("Alice", "David")

# Display network
print("=== Social Network ===")
fm.display()

# Test recommendations
print("\n=== Recommendations for Alice ===")
print(recommend_friends(fm.graph, "Alice"))

# Test undo
print("\n=== Undo last action ===")
fm.undo()
fm.display()
