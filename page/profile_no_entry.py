import flet as ft
from designer import Designer, ButtonBox

class profile_no_entry():
    def __init__(self,page:ft.Page):
        self.page=page
        
        self.page_view=ft.Column(
            controls=[
                ft.Row(
                    height=30
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            expand=True,
                            value="Кузя is everything you need,\n right next to you!",
                            size=28,
                            color=Designer.colors[4],
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.W_500
                        ),
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            #bgcolor="#000000",
                            height=300,
                            expand=True,
                            alignment=ft.alignment.top_center,
                            #content=ft.Image(
                            #   src="assets/images/Сочетание 8.svg",
                            #)
                            content=ft.Text(
                                value="Кузя",
                                size=56
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            expand=True,
                            value="Log in or register to see all the\n advantages of Кузя",
                            size=24,
                            color=Designer.colors[4],
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.W_400
                        ),
                    ]
                ),
                ft.Row(
                    height=30,    
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ButtonBox(text="Log in", metod=self.go_to_enter)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ButtonBox(text="Registration",metod=self.go_to_registration)
                    ]
                ),
            ]
        )
        
    def go_to_enter(self,e):
        self.page.go("/log")
    def go_to_registration(self,e):
        self.page.go("/reg")
        