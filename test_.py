import flet as ft

def main(page: ft.Page):
    # def page_resize(e):
    #     pw.value = f"{page.width} px"
    #     pw.update()

    # page.on_resize = page_resize

    # pw = ft.Text(bottom=50, right=50, style="displaySmall")
    # page.overlay.append(pw)
    page.add(
        ft.ResponsiveRow(

            [
                ft.Container(
                    ft.Text("Column 1"),
                    padding=5,
                    bgcolor=ft.colors.BLUE,
                    col={"sm": 12, "md": 12, "xl": 6},
                ),
                ft.Container(
                    ft.Text("Column 2"),
                    padding=5,
                    bgcolor=ft.colors.GREEN,
                    col={"sm": 2, "md": 2},
                ),


            ],
        ),
        ft.ResponsiveRow(
            [
                ft.TextField(label="TextField 1", col={"md": 4}),
                ft.TextField(label="TextField 2", col={"md": 4}),
                ft.TextField(label="TextField 3", col={"md": 4}),
            ],
            run_spacing={"xs": 10},
        ),
    )
    # page_resize(None)

ft.app(target=main)