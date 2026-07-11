# project_file_operator
📖 Journal Manager (Python)

Overview

Journal Manager is a simple command-line Python application that allows users to maintain a personal journal. Users can add journal entries, view all saved entries, search for specific entries using keywords, and delete all entries when needed.

Features

- ➕ Add new journal entries with a timestamp.
- 📄 View all saved journal entries.
- 🔍 Search journal entries by keyword.
- 🗑️ Delete all journal entries with confirmation.
- ⚠️ Handles common file-related errors using exception handling.

Technologies Used

- Python 3
- "datetime" module
- "os" module
- File Handling
- Exception Handling
- Object-Oriented Programming (OOP)

Project Structure

JournalManager/
│── journal.py
│── journal.txt   (created automatically)
│── README.md

How to Run

1. Make sure Python 3 is installed.
2. Save the code as "journal.py".
3. Open Terminal or Command Prompt.
4. Run the program:

python journal.py

Menu

_____Welcome to journal manager_____

1. Add a New Entry
2. View all Entries
3. Search for an Entry
4. Delete all Entries
5. Exit

Sample Output

Adding an Entry

Enter your choice: 1
Add a New Entry:
Enter your journal entry: Today I started learning Python.
Entry Added Successfully

Viewing Entries

Enter your choice: 2

[2026-07-11 10:15:32.654321] Today I started learning Python.

Searching an Entry

Enter your choice: 3
Enter keyword to search: Python

[2026-07-11 10:15:32.654321] Today I started learning Python.

Deleting All Entries

Enter your choice: 4
Are you sure you want to delete all entries? (yes/no): yes

All files deleted!

Exit

Enter your choice: 5

GoodBye!

Error Handling

- Displays a message if the journal file does not exist.
- Handles file permission errors.
- Prevents crashes using exception handling.

Future Improvements

- Edit existing journal entries.
- Delete a single journal entry.
- Store entries in JSON or SQLite.
- Password protection.
- Export journal entries to PDF.
- Graphical User Interface (GUI).

Author

Mohammad Taqi Panjwani
