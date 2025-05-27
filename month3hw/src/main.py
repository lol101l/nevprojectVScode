import flet as ft
from database import Database

def main(page: ft.Page):
    db = Database()
    page.title = "Список фильмов"
    page.scroll = ft.ScrollMode.AUTO

    title_field = ft.TextField(label="Название фильма", width=300)
    genre_field = ft.TextField(label="Жанр", width=300)
    year_field = ft.TextField(label="Год выхода", width=300)

    movie_table = ft.Column()
    
    def load_movies():
        movie_table.controls.clear()
        for movie in db.get_all_movies():
            movie_id, title, genre, year = movie
            row = ft.Row([
                ft.Text(f"{title} ({genre}, {year})"),
                ft.IconButton(ft.icons.DELETE, on_click=lambda e, mid=movie_id: delete_movie(mid))
            ])
            movie_table.controls.append(row)
        page.update()

    def add_movie(e):
        title = title_field.value.strip()
        genre = genre_field.value.strip()
        year = year_field.value.strip()
        if title and genre and year:
            db.add_movie(title, genre, year)
            title_field.value = ""
            genre_field.value = ""
            year_field.value = ""
            load_movies()
        page.update()

    def delete_movie(movie_id):
        db.delete_movie(movie_id)
        load_movies()

    def clear_all(e):
        db.conn.execute("DELETE FROM movies")
        db.conn.commit()
        load_movies()

    add_button = ft.ElevatedButton("Добавить", on_click=add_movie)
    clear_button = ft.TextButton("Очистить всё", on_click=clear_all)

    page.add(
        ft.Text("Добавьте фильм", size=25),
        title_field,
        genre_field,
        year_field,
        ft.Row([add_button, clear_button]),
        ft.Divider(),
        movie_table
    )

    load_movies()

ft.app(target=main)
