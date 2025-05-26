import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL
        )
        """)
        self.conn.commit()

    def add(self, name, amount):
        self.conn.execute("INSERT INTO expenses (name, amount) VALUES (?, ?)", (name, amount))
        self.conn.commit()

    def delete(self, exp_id):
        self.conn.execute("DELETE FROM expenses WHERE id = ?", (exp_id,))
        self.conn.commit()

    def update(self, exp_id, new_name, new_amt):
        self.conn.execute("UPDATE expenses SET name = ?, amount = ? WHERE id = ?", (new_name, new_amt, exp_id))
        self.conn.commit()

    def get_all(self):
        return self.conn.execute("SELECT id, name, amount FROM expenses").fetchall()

    def get_total(self):
        row = self.conn.execute("SELECT SUM(amount) FROM expenses").fetchone()
        return row[0] if row[0] else 0