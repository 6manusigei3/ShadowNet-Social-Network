from system.friend_manager import FriendManager

fm = FriendManager()

fm.create_user("Alice")
fm.create_user("Bob")
fm.create_user("Carol")

fm.add_friend("Alice", "Bob")
fm.add_friend("Bob", "Carol")

fm.display()
