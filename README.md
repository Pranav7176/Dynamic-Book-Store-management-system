-> Dynamic Bookstore Management System:
A command-line bookstore management system built with Python and SQLite.
This started as a basic Python OOP project and evolved into a fully 
database-backed application, because data should never die when the 
program closes.

-> What it does:
- Browse all available books in the store
- Lend books to users (tracked in database)
- Return books back to the store
- Add new books to the collection
- All data persists permanently using SQLite

-> Built with:
- Python 3 (OOP)
- SQLite via pysqlite3
- SQLiteStudio (for database visualization)

-> How to run:
1. Clone the repo
2. Make sure you have Python installed
3. Install pysqlite3
   pip install pysqlite3
4. Run the program
   python main.py

-> Why I built this:
Started as a Python OOP exercise. Then I asked myself,
what happens to all this data when the program closes?
That question led me to integrate SQLite and rebuild the 
entire storage layer. v1 used lists and dictionaries. 
v2 uses a real database.

-> What's next:
- Flask REST API wrapper
- Web frontend
- Multi-store support
