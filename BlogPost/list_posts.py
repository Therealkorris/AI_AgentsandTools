
import os

def list_posts():
    # List all text files in the current directory
    posts = [f for f in os.listdir() if f.endswith('.txt')]

    if posts:
        print("Here are all the posts:")
        for post in posts:
            print(post.replace('.txt', ''))
    else:
        print("There are no posts.")

if __name__ == "__main__":
    list_posts()
    