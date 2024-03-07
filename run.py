from app import Blog


def run_blog():
    print('Welcome to the Kekambas Blog!')
    # Create an instance of the blog class
    blog = Blog()
    # Start "running" our blog until user quits
    while True:
        # Print the menu option
        print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
        # Ask the user what they would like to do
        to_do = input('Which option would you like to do? ')
        # Make sure they give a valid option
        while to_do not in {'1', '2', '3', '4', '5'}:
            to_do = input('Invalid option. Please enter 1, 2, 3, 4, or 5: ')
        # Different "routes" - different options to take
        if to_do == '5':
            break
        elif to_do == '1':
            # Call the create_new_user method on the blog
            blog.create_new_user()
        else:
            print(f"Option {to_do} is coming soon!")
    # Once the user quits and the while loop breaks
    print("Thank you for checking out the blog")
    print(blog.users)
    print(blog.posts)


run_blog()