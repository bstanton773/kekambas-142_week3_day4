from .models import User, Post

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

    # Method to add a new post to the blog, authored by the logged in user
    def create_new_post(self):
        # Check to make sure that we have a lgged in user
        if self.current_user is None:
            print('You must be logged in to perform this action') # 401 Unauthorized
        else:
            # Get the title and post from the user input
            title = input('Enter new post title: ')
            body = input('Enter new post body: ')
            # Create a new instance of Post with the inputted info + logged in user
            new_post = Post(title, body, self.current_user)
            # Add the new post to the blog's list of posts
            self.posts.append(new_post)
            print(f"{new_post.title} has been created!")

    # Method to view all of the posts in the blog
    def view_posts(self):
        # Check if there are any posts
        if self.posts:
            # Loop through the posts
            for post in self.posts:
                # Print the post (the __str__ method will format it for us)
                print(post)
        # If no posts
        else:
            print('There are currently no posts in this blog :( ')
