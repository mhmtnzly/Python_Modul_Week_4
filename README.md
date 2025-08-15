# Python_Modul_Week_4

# 📚 Mini Book Management System

This project is a beginner-friendly book management system built with Python. It allows users to manage a collection of books through a simple command-line interface. All data is stored in a JSON file for persistence.

## 🚀 Features

- Add a book (interactive input for each field)
- Remove a book (by title)
- Update book details
- Search for a book (by title)
- List all books

## 🗂️ Book Format

Each book is stored in the following format inside the `books.json` file:

```json
{
  "title": "1984",
  "author": "George Orwell",
  "year": 1949,
  "genre": "Dystopian"
}
```

## 🛠️ Technologies Used

- Python 3.x
- JSON module (built-in)

## 📁 File Structure

```
mini_book_system.py       # Main script
books.json                # Data file storing all books
```

## 📌 Installation & Usage

1. Make sure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/yourUsername/mini_book_system.git
   ```
3. Run the script:
   ```bash
   python mini_book_system.py
   ```

## 📄 How It Works

When you run the program, you'll be presented with a menu:

```
1. Add a book
2. Remove a book
3. Update a book
4. Search for a book
5. List all books
6. Exit
```

### ➕ Add a Book

You will be prompted to enter each field one by one:

```
Enter book title:
Enter author name:
Enter publication year:
Enter genre:
```

The book will be saved in `books.json`.

### ➖ Remove a Book

You will be asked to enter the title of the book to remove. If found, it will be deleted from the JSON file.

### ✏️ Update a Book

You can update any field of a book by entering its title and then choosing which field to modify.

### 🔍 Search for a Book

Search by title. If found, the book's details will be displayed.

### 📋 List All Books

Displays all books currently stored in the JSON file.

## 🎯 Purpose

This project is ideal for Python learners who want to practice:

- File handling with JSON
- User input and validation
- Basic CRUD operations
- Modular and interactive programming

## 📬 Contribute

Feel free to fork the project and submit pull requests to improve functionality or add new features!

---

Made with ❤️ by Mehmet
