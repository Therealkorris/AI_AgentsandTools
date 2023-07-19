
import os

def write_post():
    title = input("Enter the title of your post: ")
    content = input("Enter the content of your post: ")

    # Save the post in a text file
    with open(f"{title}.txt", 'w') as f:
        f.write(content)

    print(f"Post '{title}' has been saved.")

if __name__ == "__main__":
    write_post()
    