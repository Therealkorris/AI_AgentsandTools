
import os

def edit_post():
    title = input("Enter the title of the post you want to edit: ")

    # Check if the post exists
    if os.path.exists(f"{title}.txt"):
        # Load the existing content
        with open(f"{title}.txt", 'r') as f:
            content = f.read()

        print(f"Current content of the post '{title}':")
        print(content)

        # Ask for the new content
        new_content = input("Enter the new content of the post: ")

        # Save the new content
        with open(f"{title}.txt", 'w') as f:
            f.write(new_content)

        print(f"Post '{title}' has been updated.")
    else:
        print(f"Post '{title}' does not exist.")

if __name__ == "__main__":
    edit_post()
    