import random

class User:
    def __init__(self, name, age, gender, preferences):
        self.name = name
        self.age = age
        self.gender = gender
        self.preferences = preferences
        self.likes = []
        self.matches = []
        self.messages = []

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}, {self.preferences}"

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.read = False

    def __str__(self):
        return f"From: {self.sender.name}, To: {self.receiver.name}, Content: {self.content}"

class DatingApp:
    def __init__(self):
        self.users = []
        self.messages = []

    def register_user(self, name, age, gender, preferences):
        user = User(name, age, gender, preferences)
        self.users.append(user)

    def like_user(self, user, liked_user):
        if liked_user.gender != user.gender:
            user.likes.append(liked_user)

    def match_users(self):
        for user in self.users:
            potential_matches = [u for u in user.likes if u in self.users and user in u.likes and user.preferences == u.gender]
            if potential_matches:
                for match in potential_matches:
                    user.matches.append(match)
                    match.matches.append(user)

    def send_message(self, sender, receiver, content):
        message = Message(sender, receiver, content)
        self.messages.append(message)
        sender.messages.append(message)
        receiver.messages.append(message)

    def display_matches(self):
        for user in self.users:
            print(f"{user.name}'s matches:")
            for match in user.matches:
                print(f"\t{match}")

    def display_messages(self, user):
        unread_messages = [m for m in user.messages if not m.read and m.receiver == user]
        if unread_messages:
            print(f"Unread messages for {user.name}:")
            for message in unread_messages:
                print(f"\t{message}")
                message.read = True
        else:
            print(f"No unread messages for {user.name}")

def main():
    app = DatingApp()

    app.register_user("Alice", 25, "Female", "Male")
    app.register_user("Bob", 30, "Male", "Female")
    app.register_user("Charlie", 28, "Male", "Female")
    app.register_user("David", 23, "Male", "Female")
    app.register_user("Eve", 27, "Female", "Male")
    app.register_user("Fiona", 29, "Female", "Male")

    users = app.users
    for _ in range(20):
        user = random.choice(users)
        liked_user = random.choice(users)
        app.like_user(user, liked_user)

    app.match_users()

    for user in app.users:
        matches = user.matches
        if matches:
            for _ in range(random.randint(1, 5)):
                match = random.choice(matches)
                content = f"Hi {match.name}, this is {user.name}."
                app.send_message(user, match, content)

    for user in app.users:
        app.display_matches()
        app.display_messages(user)

if __name__ == "__main__":
    main()

class UserProfile:
    def __init__(self, user, bio="", interests=None, photos=None):
        self.user = user
        self.bio = bio
        self.interests = interests if interests else []
        self.photos = photos if photos else []

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_photo(self, photo):
        self.photos.append(photo)

class Authentication:
    def __init__(self):
        self.logged_in_users = []

    def login(self, username, password):
        # Simulate authentication process
        if username == "admin" and password == "admin":
            self.logged_in_users.append(username)
            return True
        else:
            return False

    def logout(self, username):
        self.logged_in_users.remove(username)

class DatingApp:
    def __init__(self):
        self.users = []
        self.user_profiles = {}
        self.messages = []

    def register_user(self, username, password, name, age, gender, preferences):
        user = User(name, age, gender, preferences)
        self.users.append(user)
        self.user_profiles[username] = UserProfile(user)
        return user

    def authenticate_user(self, username, password):
        auth = Authentication()
        if auth.login(username, password):
            return self.user_profiles[username]
        else:
            return None

    def like_user(self, user, liked_user):
        if liked_user.gender != user.gender:
            user.likes.append(liked_user)

    def match_users(self):
        for user in self.users:
            potential_matches = [u for u in user.likes if u in self.users and user in u.likes and user.preferences == u.gender]
            if potential_matches:
                for match in potential_matches:
                    user.matches.append(match)
                    match.matches.append(user)

    def send_message(self, sender, receiver, content):
        message = Message(sender, receiver, content)
        self.messages.append(message)
        sender.messages.append(message)
        receiver.messages.append(message)

    def display_matches(self, user):
        matches = user.matches
        if matches:
            print(f"{user.name}'s matches:")
            for match in matches:
                print(f"\t{match}")
        else:
            print(f"{user.name} has no matches yet.")

    def display_messages(self, user):
        unread_messages = [m for m in user.messages if not m.read and m.receiver == user]
        if unread_messages:
            print(f"Unread messages for {user.name}:")
            for message in unread_messages:
                print(f"\t{message}")
                message.read = True
        else:
            print(f"No unread messages for {user.name}")

def main():
    app = DatingApp()

    # Register users
    user1 = app.register_user("user1", "password1", "Alice", 25, "Female", "Male")
    user2 = app.register_user("user2", "password2", "Bob", 30, "Male", "Female")
    user3 = app.register_user("user3", "password3", "Charlie", 28, "Male", "Female")
    user4 = app.register_user("user4", "password4", "David", 23, "Male", "Female")
    user5 = app.register_user("user5", "password5", "Eve", 27, "Female", "Male")
    user6 = app.register_user("user6", "password6", "Fiona", 29, "Female", "Male")

    # Like users
    app.like_user(user1, user2)
    app.like_user(user2, user1)
    app.like_user(user3, user1)
    app.like_user(user1, user3)

    # Match users
    app.match_users()

    # Display matches and unread messages
    user_profiles = app.user_profiles
    for username, profile in user_profiles.items():
        print(f"Matches and messages for {username}:")
        app.display_matches(profile.user)
        app.display_messages(profile.user)

if __name__ == "__main__":
    main()
