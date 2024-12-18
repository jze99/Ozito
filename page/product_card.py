import flet as ft
from designer import Designer,TextField
from user_data import user_data_class as udc
import requests
import json

class product_card():
    product_id = 0
    creator_id = 0
    name_page = "order"
    price_page = 0
    Categorial_page = ""
    Description_page = ""
    def __init__(self, page:ft.Page):
        self.page = page
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
                            content=ft.Text(value=product_card.name_page,size=26, color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            #bgcolor="#1529DD",
                            #content=ft.IconButton(hover_color=Designer.colors[0],icon=ft.icons.DELETE_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
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
                                    bgcolor=Designer.colors[0],
                                    image=ft.DecorationImage(src=f"http://31.31.196.6:8000/ozito/get_image?file_name={product_card.creator_id}{product_card.product_id}.png")
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="Price:", size=22,color=Designer.colors[4]),
                                        ft.Text(value=str(product_card.price_page) + " RUB.", size=22,color=Designer.colors[4]),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="Category:", size=22,color=Designer.colors[4]),
                                        ft.Text(value=product_card.Categorial_page, size=22,color=Designer.colors[4]),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(value="Description:", size=22,color=Designer.colors[4]),
                                        ft.Text(value=product_card.Description_page, size=22,color=Designer.colors[4]),        
                                    ]
                                ),
                            ]
                        )
                    ]
                ),
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="Creator's phone number:", size=22,color=Designer.colors[4]),
                        ft.Text(value=self.find_creator_phone(), size=22,color=Designer.colors[4]),    
                    ]
                )
            ]
        )
    def find_creator_phone(self):
        r = requests.get("http://31.31.196.6:8000/ozito/select_all_users")
        users = json.loads(r.content)

        if users is not None:
            for user in users["data"]:
                if user["id"] == self.creator_id:
                    return str(user["phone_number"])
        else:
            return "89999999999"        
    
        
    def go_to_orders(self,e):
        self.page.go("/search")