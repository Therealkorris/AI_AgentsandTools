
import os

def delete_post():
    title = input("Enter the title of the post you want to delete: ")

    # Check if the post exists
    if os.path.exists(f"{title}.txt"):
        # Delete the post
        os.remove(f"{title}.txt")

        print(f"Post '{title}' has been deleted.")
    else:
        print(f"Post '{title}' does not exist.")

if __name__ == "__main__":
    delete_post()
    