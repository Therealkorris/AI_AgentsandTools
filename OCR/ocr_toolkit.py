
import os
from extract_text_from_image import extract_text_from_image
from extract_text_from_pdf import extract_text_from_pdf

def ocr_toolkit():
    while True:
        print("\nOCR Toolkit")
        print("1. Extract text from an image")
        print("2. Extract text from a PDF")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            extract_text_from_image()
        elif choice == '2':
            extract_text_from_pdf()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    ocr_toolkit()
    