import json
import os

BOOKS_FILE = "books.json"

def load_books():
    """
    Load books from the JSON file.
    - Check if the file exists.
    - If it does, open and parse the JSON content.
    - If it doesn't exist or is empty, return an empty list.
    """
    pass  # TODO: Implement file reading and JSON parsing

def save_books(books):
    """
    Save the list of books to the JSON file.
    - Open the file in write mode.
    - Convert the list of dictionaries to JSON format.
    - Use indentation for readability.
    """
    pass  # TODO: Implement file writing and JSON dumping

def add_book():
    """
    Add a new book to the collection.
    - Prompt the user for title, author, year, and genre.
    - Create a dictionary with this data.
    - Load existing books, append the new one, and save.
    """
    pass  # TODO: Implement user input and book addition logic

def remove_book():
    """
    Remove a book by title.
    - Ask the user for the title of the book to remove.
    - Load the book list and filter out the matching title.
    - Save the updated list back to the file.
    """
    pass  # TODO: Implement book removal logic

def update_book():
    """
    Update details of an existing book.
    - Ask for the title of the book to update.
    - If found, ask which field to update (title, author, year, genre).
    - Modify the selected field and save changes.
    """
    pass  # TODO: Implement book update logic

def search_book():
    """
    Search for books by title keyword.
    - Ask the user for a keyword.
    - Load books and find matches where the title contains the keyword.
    - Display matching books.
    """
    pass  # TODO: Implement search functionality

def list_books():
    """
    List all books in the collection.
    - Load books from the file.
    - Print each book's details in a readable format.
    """
    pass  # TODO: Implement listing logic

def print_book(book):
    """
    Print details of a single book.
    - Display title, author, year, and genre.
    """
    pass  # TODO: Implement formatted printing of book info

def main():
    """
    Main menu loop.
    - Display options to the user.
    - Call the corresponding function based on user input.
    - Repeat until the user chooses to exit.
    """
    pass  # TODO: Implement menu logic and user interaction

if __name__ == "__main__":
    main()
