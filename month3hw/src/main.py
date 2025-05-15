import flet as ft
from database import Database

def main(page: ft.Page):
    db = Database()
    page.title = "Учёт расходов"
    page.vertical_alignment = ft.MainAxisAlignment.START

    title = ft.Text("Ваши расходы", size=30)
    name_input = ft.TextField(label="Название расхода", width=300)
    amount_input = ft.TextField(label="Сумма расхода", width=300)
    expense_list = ft.Column()
    total_text = ft.Text("Общая сумма: 0 руб.")
    total_sum = 0.0

    def add_expense(e):
        nonlocal total_sum

        name = name_input.value
        try:
            amount = float(amount_input.value)
        except ValueError:
            amount_input.error_text = "Введите корректное число"
            page.update()
            return

        db.add_expense(name, amount)
        expense_list.controls.append(ft.Text(f"{name}: {amount:.2f} руб."))
        total_sum += amount
        total_text.value = f"Общая сумма: {total_sum:.2f} руб."

        name_input.value = ""
        amount_input.value = ""
        amount_input.error_text = None
        page.update()

    add_button = ft.ElevatedButton(text="Добавить", on_click=add_expense)

    page.add(title, name_input, amount_input, add_button, expense_list, total_text)

ft.app(target=main)