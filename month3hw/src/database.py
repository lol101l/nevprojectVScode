import sqlite3

class Database:
    def init(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, name, amount):
        query = "INSERT INTO expenses (name, amount) VALUES (?, ?);"
        self.conn.execute(query, (name, amount))
        self.conn.commit()