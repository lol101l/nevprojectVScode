import flet as ft
from database import Database

def main(page: ft.Page):
    db = Database()
    page.title = "Учёт расходов"
    page.vertical_alignment = ft.MainAxisAlignment.START

    title = ft.Text("Ваши расходы", size=30)
    name_input = ft.TextField(label="Название", width=300)
    amount_input = ft.TextField(label="Сумма", width=300)

    list_exp = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    txt_total = ft.Text()

    def update_total():
        txt_total.value = "Общая сумма: " + str(db.get_total()) + " руб."
        page.update()

    def load_expenses():
        list_exp.controls.clear()
        for exp_id, name, amt in db.get_all():
            row = make_expense_row(exp_id, name, amt)
            list_exp.controls.append(row)
        update_total()

    def make_expense_row(exp_id, name, amt):
        text = ft.Text(f"{name}: {amt} руб.")

        def delete(e):
            db.delete(exp_id)
            load_expenses()

        def edit(e):
            name_field = ft.TextField(label="Название", value=name)
            amt_field = ft.TextField(label="Сумма", value=str(amt))

            def save_edit(btn):
                try:
                    new_amt = float(amt_field.value)
                    db.update(exp_id, name_field.value, new_amt)
                    dlg.open = False
                    load_expenses()
                except:
                    amt_field.error_text = "Ошибка в числе"
                    dlg.update()

            dlg.content = ft.Column([
                name_field,
                amt_field
            ])
            dlg.actions = [
                ft.TextButton("Сохранить", on_click=save_edit),
                ft.TextButton("Отмена", on_click=lambda _: close_dlg())
            ]
            dlg.open = True
            page.update()

        return ft.Row([
            text,
            ft.IconButton(ft.icons.EDIT, on_click=edit),
            ft.IconButton(ft.icons.DELETE, on_click=delete)
        ])

    def close_dlg():
        dlg.open = False
        page.update()

    def add_expense(e):
        name = name_input.value
        try:
            amt = float(amount_input.value)
            db.add(name, amt)
            name_input.value = ""
            amount_input.value = ""
            load_expenses()
        except:
            amount_input.error_text = "Ошибка"
            page.update()

    btn_add = ft.ElevatedButton("Добавить", on_click=add_expense)
    dlg = ft.AlertDialog(open=False)
    page.dialog = dlg

    load_expenses()

    page.add(
        title,
        name_input,
        amount_input,
        btn_add,
        list_exp,
        txt_total
    )

ft.app(target=main)