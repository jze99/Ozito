import flet as ft
from designer import Designer,OrderRow
import requests
from user_data import user_data_class as udc

class my_order():
    def __init__(self, page:ft.Page):
        self.page=page
        
        self.orders = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment=ft.MainAxisAlignment.START,
            controls= self.load_user_products()
        )
        self.page_view=ft.Column(
            expand=True,
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
                ft.Row(
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        self.orders
                    ]    
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            on_click=self.go_to_create_order,
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
    def load_user_products(self):
        r = requests.get("http://31.31.196.6:8000/ozito/select_all_products")
        prod_js = r.json()
        prods = []
        for p in prod_js["data"]:
            if p["creator_id"] == udc.id:
                prods.append(OrderRow(p["product_id"], p["product_name"], p["product_description"], p["price"], p["creator_id"], p["category"],
                                      p["status"]))
        return prods
        
    def go_to_create_order(self,e):
        self.page.go("/new_order")
    
    def go_to_account(self,e):
        self.page.go("/prof_entry")
        