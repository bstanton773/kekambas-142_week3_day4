from .models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []

    # Method to create a new user instance and add to the Blog's user list
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check to see if a user with that username already exists
        while username in {u.username for u in self.users}:
            print(f"User with username {username} already exists")
            username = input('Enter a different username: ')
        
        password = input('Please enter a password: ')
        # Create an instance of User with the inputted info
        new_user = User(username, password)
        # Add the new instance of user to the blog's user list
        self.users.append(new_user)
        print(f"{new_user} has been created.")

