class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, role):
        """Add a new user with a specified role."""
        if username in self.users:
            print(f"User {username} already exists.")
        else:
            self.users[username] = role
            print(f"User {username} added with role {role}.")

    def remove_user(self, username):
        """Remove a user by username."""
        if username in self.users:
            del self.users[username]
            print(f"User {username} removed.")
        else:
            print(f"User {username} does not exist.")

    def list_users(self):
        """List all users and their roles."""
        print("Current users:")
        for username, role in self.users.items():
            print(f" - {username}: {role}")

if __name__ == "__main__":
    # Example usage
    user_manager = UserManager()
    user_manager.add_user("alice", "admin")
    user_manager.add_user("bob", "editor")
    user_manager.list_users()
    user_manager.remove_user("alice")
    user_manager.list_users()
