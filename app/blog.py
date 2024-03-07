from .models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

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

    # Method to log a user in
    def log_user_in(self):
        # Ask the user for credentials
        username_input = input('What is your username? ')
        password_input = input('What is your password? ')
        # Loop through the users in the blog's user list
        for user in self.users:
            # Check if the user's username matches the username_input - same with password
            if user.username == username_input and user.check_password(password_input):
                # If both are True, set the blog's current user to that user
                self.current_user = user
                print(f"{user} has logged in.")
                # Once we find the right user, we don't know check any other users
                break
        # if we go through the loop without breaking
        else:
            # Then the user has bad credentials
            print('Username and/or password is incorrect.')

    # Method to log a user out
    def log_user_out(self):
        print(f"{self.current_user} has been logged out.")
        self.current_user = None

