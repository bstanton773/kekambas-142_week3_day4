from .models import User, Post

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

    # Private method that will get a post by its ID or return None if no post with that ID
    def __get_post_from_id(self):
        # Ask the user for the ID of the post they would like to view
        post_id = input('What is the ID of the post that you would like to get? ')
        # Ensure that we can convert our post_id to an integer
        while not post_id.isdigit():
            post_id = input('Invalid ID. Must be an integer. Please enter ID again: ')
        # Loop through all of the posts in the blog
        for post in self.posts:
            # If the post's ID matches the post_id argument
            if post.id == int(post_id):
                # Return that post instance
                return post
        # If we finish the loop, that means we did not find a post with that ID
        print(f"Post with an ID of {post_id} does not exist") # 404 Not Found

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

    # Method to view a single post by ID
    def view_post(self):
        # Get the post using the private method
        post = self.__get_post_from_id()
        # Check if the post exists
        if post:
            # If so, print that post
            print(post)

    # Method to edit a post by ID
    def edit_post(self):
        post = self.__get_post_from_id()
        if post:
            # Check to see that the logged in user is the author of the post
            if post.author == self.current_user:
                # print the post so they can see what they are editing
                print(post)

                # Ask for the new title of the post or have them skip to keep the current title
                new_title = input("Enter a new title or type 'skip' to keep the current title: ")
                if new_title.lower() != 'skip':
                    # Set the title attribute on the post to the new title
                    post.title = new_title

                # Ask for the new body of the post or have them skip to keep the current body
                new_body = input("Enter a new body or type 'skip' to keep the current body: ")
                if new_body.lower() != 'skip':
                    # Set the body attribute on the post to the new body
                    post.body = new_body

                print(f"{post.title} has been updated!")
            # If the user is logged in but not the author
            elif self.current_user is not None:
                print("You do not have permission to edit this post.") # 403 Forbidden
            # If the user is not logged in at all
            else:
                print("You must be logged in to perform this action.") # 401 Unauthorized
