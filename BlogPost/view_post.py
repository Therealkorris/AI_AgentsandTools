
import os

def view_post():
    title = input("Enter the title of the post you want to view: ")

    # Check if the post exists
    if os.path.exists(f"{title}.txt"):
        # Load the content
        with open(f"{title}.txt", 'r') as f:
            content = f.read()

        print(f"Content of the post '{title}':")
        print(content)
    else:
        print(f"Post '{title}' does not exist.")

if __name__ == "__main__":
    view_post()
    