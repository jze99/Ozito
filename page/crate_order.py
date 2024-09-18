import flet as ft
from designer import Designer,TextField
import user_data

class create_order_page():
    def __init__(self, page:ft.Page):
        self.page = page
        self.name_order = TextField()
        self.price_order = TextField()
        self.Categorial_order = TextField()
        self.Description_order = TextField()
        self.page_view=ft.Column(
            expand=True,
            controls=[
                ft.Row( #top row
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center_left,
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.IconButton(on_click=self.go_to_orders,hover_color=Designer.colors[0],icon=ft.icons.ARROW_BACK_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            #bgcolor="#FF0000",
                            content=ft.Text(value="New order",size=26, color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            #bgcolor="#1529DD",
                            #content=ft.IconButton(on_click=self.go_to_seting,hover_color=Designer.colors[0],icon=ft.icons.SETTINGS_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                    ]
                ),
                ft.Row(
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            #expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            
                            controls=[
                                ft.Container(
                                    height=200,
                                    width=200,
                                    border_radius=ft.border_radius.all(10),
                                    bgcolor=Designer.colors[0]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="name:", size=22,color=Designer.colors[4]),
                                        self.name_order
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="Price:", size=22,color=Designer.colors[4]),
                                        self.price_order
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="Categorical:", size=22,color=Designer.colors[4]),
                                        self.Categorial_order
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="Description:", size=22,color=Designer.colors[4]),
                                        self.Description_order
                                    ]
                                ),
                            ]
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            on_click=self.go_to_orders,
                            alignment=ft.alignment.center,
                            height=80,
                            bgcolor=Designer.colors[0],
                            expand=True,
                            content=ft.Text(
                                value="Create order",
                                size=28,
                                color=Designer.colors[4]
                            )
                        )    
                    ]
                )
            ]
        )
        
    def go_to_orders(self,e):
        self.page.go("/my_orders")