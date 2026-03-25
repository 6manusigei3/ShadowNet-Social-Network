from system.friend_manager import FriendManager

def run_tests():
    fm = FriendManager()

    fm.create_user("Alice")
    fm.create_user("Bob")

    fm.add_friend("Alice", "Bob")

    assert "Bob" in fm.show_friends("Alice")

    print("All tests passed!")

run_tests()
