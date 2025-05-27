import sqlite3

class Database:
    def __init__(self, db_name="db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            genre TEXT,
            year TEXT
        )
        """)
        self.conn.commit()

    def add_movie(self, title, genre, year):
        self.conn.execute("INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)", (title, genre, year))
        self.conn.commit()

    def delete_movie(self, movie_id):
        self.conn.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        self.conn.commit()

    def get_all_movies(self):
        return self.conn.execute("SELECT id, title, genre, year FROM movies").fetchall()