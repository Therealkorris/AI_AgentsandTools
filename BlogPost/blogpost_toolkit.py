
import os
from write_post import write_post
from edit_post import edit_post
from delete_post import delete_post
from view_post import view_post
from list_posts import list_posts

def blogpost_toolkit():
    while True:
        print("\nBlogPost Toolkit")
        print("1. Write a new post")
        print("2. Edit an existing post")
        print("3. Delete a post")
        print("4. View a post")
        print("5. List all posts")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            write_post()
        elif choice == '2':
            edit_post()
        elif choice == '3':
            delete_post()
        elif choice == '4':
            view_post()
        elif choice == '5':
            list_posts()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    blogpost_toolkit()
    