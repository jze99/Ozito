import flet as ft
from designer import Designer,OrderRow

class my_order():
    def __init__(self, page:ft.Page):
        self.page=page
        
        self.orders = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                OrderRow(),
            ]
        )
        self.page_view=ft.Column(
            controls=[
                ft.Row( #top row
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center_left,
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.IconButton(on_click=self.go_to_account,hover_color=Designer.colors[0],icon=ft.icons.ARROW_BACK_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            #bgcolor="#FF0000",
                            content=ft.Text(value="My orders",size=26, color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            #bgcolor="#1529DD",
                            #content=ft.IconButton(on_click=self.go_to_seting,hover_color=Designer.colors[0],icon=ft.icons.SETTINGS_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                    ]
                ),
                self.orders
            ]
        )
    
    def go_to_account(self,e):
        self.page.go("/prof_entry")
        