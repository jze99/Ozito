import flet as ft
from designer import Designer
from user_data import user_data_class
import requests

class profile():
    def __init__(self, page:ft.Page):
        self.count = 0
        self.page = page
        self.page_view=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                ft.Row( #top row
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center_left,
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.IconButton(on_click=self.go_to_search,hover_color=Designer.colors[0],icon=ft.icons.ARROW_BACK_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            #bgcolor="#FF0000",
                            content=ft.Text(value="Account",size=26, color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            #bgcolor="#1529DD",
                            content=ft.IconButton(on_click=self.go_to_seting,hover_color=Designer.colors[0],icon=ft.icons.SETTINGS_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                    ]
                ),
                ft.Row(#prof data
                    controls=[
                        ft.Container(
                            bgcolor=Designer.colors[3],
                            expand=True,
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.CircleAvatar(
                                                content=ft.Icon(ft.icons.ABC),
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Login:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            ft.Text(
                                                value=user_data_class.name,
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                        ]    
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Role:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            ft.Text(
                                                value=user_data_class.role,
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                        ]    
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Phone number:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            ft.Text(
                                                value=user_data_class.phone_number,
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value=user_data_class.rating,
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            ft.Icon(
                                                name=ft.icons.STAR_ROUNDED,
                                                size=30,
                                                color=Designer.colors[0]
                                            )
                                        ]
                                    ),
                                ]    
                            ),
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(#orders container
                            bgcolor=Designer.colors[3],
                            expand=True,
                            on_click=self.go_to_my_orders,
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Orders",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.EDIT_DOCUMENT,
                                                size=50,
                                                color=Designer.colors[4],
                                            ),
                                            ft.Text(
                                                value="Your orders:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                            ft.Text(
                                                value=self.user_order_count(),
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                        ]    
                                    ),
                                ]
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(#adres container
                            bgcolor=Designer.colors[3],
                            expand=True,
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Address:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.HOME_ROUNDED,
                                                size=50,
                                                color=Designer.colors[4],
                                            ),
                                            ft.Text(
                                                value="Your address:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                            ft.Text(
                                                value=user_data_class.address,
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                        ]    
                                    ),
                                ]
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(#mail container
                            bgcolor=Designer.colors[3],
                            expand=True,
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="E-mail:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.ALTERNATE_EMAIL_ROUNDED,
                                                size=50,
                                                color=Designer.colors[4],
                                            ),
                                            ft.Text(
                                                value="Your E-mail:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                            ft.Text(
                                                value=user_data_class.email,
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                        ]    
                                    ),
                                ]
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            expand=True,
                            height=50,
                            alignment=ft.alignment.center,
                            bgcolor=Designer.colors[0],
                            content=ft.Text(value="Log out", size=22,color=Designer.colors[4]),
                            on_click=self.logout
                        )
                    ]
                )
            ]
        )
    def user_order_count(self):
        count = 0
        r = requests.get("http://31.31.196.6:8000/ozito/select_all_products")
        prod_js = r.json()
        for p in prod_js["data"]:
            if p["creator_id"] == user_data_class.id and p["status"] == "Выставлен":
                count += 1
        return count
        
    def go_to_my_orders(self,e):
        self.page.go("/my_orders")
    def go_to_search(self,e):
        self.page.go("/search")
    def go_to_seting(self,e):
        self.page.go("/seting")
    
    def logout(self, e):
        self.page.go("/prof_no_entry")