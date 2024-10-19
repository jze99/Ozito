import flet as ft
from designer import Designer,TextField
import user_data
import requests

class order_page():
    p_id = 0
    c_id = 0
    name_page = "order"
    price_page = 0
    Categorial_page = ""
    Description_page = ""
    status_page = ""
    def __init__(self, page:ft.Page):
        self.page = page
        self.p_id = order_page.p_id
        self.c_id = order_page.c_id
        self.name_order = TextField(value=order_page.name_page)
        self.price_order = TextField(value=order_page.price_page)
        self.Categorial_order = TextField(value=order_page.Categorial_page)
        self.Description_order = TextField(value=order_page.Description_page)
        self.status_order = order_page.status_page
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
                            content=ft.Text(value=order_page.name_page,size=26, color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            #bgcolor="#1529DD",
                            content=ft.IconButton(hover_color=Designer.colors[0],icon=ft.icons.DELETE_ROUNDED,icon_size=35,
                                                  icon_color=Designer.colors[4], on_click=self.delete_product)
                        ),
                    ]
                ),
                ft.Row(
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
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
                                        ft.Text(value="Name:", size=22,color=Designer.colors[4]),
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
                                        ft.Text(value="Category:", size=22,color=Designer.colors[4]),
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
                            on_click=self.save_product,
                            alignment=ft.alignment.center,
                            height=80,
                            bgcolor=Designer.colors[0],
                            expand=True,
                            content=ft.Text(
                                value="Save order",
                                size=28,
                                color=Designer.colors[4]
                            )
                        )    
                    ]
                )
            ]
        )
    def delete_product(self, e):
        if self.status_order == "Выставлен":
            r = requests.delete("http://31.31.196.6:8000/ozito/delete_product?id="+str(self.p_id))
            self.page.go("/my_orders")
        else:
            pass
        
    def save_product(self, e):
        if self.status_order ==  "Выставлен":
            if self.name_order.value != "" and self.price_order.value != "" and self.Categorial_order.value != "" and self.Description_order.value != "":
                if self.price_order.value.isnumeric():
                    r = requests.put("http://31.31.196.6:8000/ozito/update_product?id="+str(self.p_id)+
                            "&product_name="+self.name_order.value+"&product_description="+
                            self.Description_order.value+"&price="+self.price_order.value+"&creator_id="+str(self.c_id)
                            +"&status=%D0%92%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD&category="+self.Categorial_order)
                    self.page.go("/my_orders")
                else:
                    pass
            else:
                pass
        else:
            pass
    
    def go_to_orders(self,e):
        self.page.go("/my_orders")