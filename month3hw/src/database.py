import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
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

    def get_total_sum(self):
        query = "SELECT SUM(amount) FROM expenses;"
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0.0