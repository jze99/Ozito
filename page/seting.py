import flet as ft
from designer import Designer, TextField, Button
from user_data import user_data_class
import requests

class seting():
    def __init__(self, page:ft.Page):
        self.page = page
        self.name_text = TextField(value=user_data_class.name)
        self.password_text = TextField()
        self.phone_number_text = TextField(value=user_data_class.phone_number)
        self.address_text = TextField(value=user_data_class.address)
        self.email_text  = TextField(value=user_data_class.email)
        self.current_password_text = TextField(password=True, can_reveal_password=True)
        self.new_password_text = TextField(password=True,can_reveal_password=True)
        self.confirm_the_password_text = TextField(password=True,can_reveal_password=True)
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
                            #content=ft.IconButton(on_click=self.go_to_seting,hover_color=Designer.colors[0],icon=ft.icons.SETTINGS_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
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
                                                value="name:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            self.name_text
                                        ]    
                                    ),
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Text(
                                                value="Phone number:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            self.phone_number_text
                                        ]
                                    ),
                                    #ft.Row(
                                    #    controls=[
                                    #        ft.Text(
                                    #            value=user_data_class.rating,
                                    #            color=Designer.colors[4],
                                    #            size=22,
                                    #        ),
                                    #        ft.Icon(
                                    #            name=ft.icons.STAR_ROUNDED,
                                    #            size=30,
                                    #            color=Designer.colors[0]
                                    #        )
                                    #    ]
                                    #),
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Text(
                                                value="The current password:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            self.current_password_text
                                        ]
                                    ),
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Text(
                                                value="New password:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            self.new_password_text
                                        ]
                                    ),
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Text(
                                                value="confirm:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            self.confirm_the_password_text
                                        ]
                                    ),
                                ]    
                            ),
                        )
                    ]
                ),
                #ft.Row(
                #    controls=[
                #        ft.Container(#orders container
                #            bgcolor=Designer.colors[3],
                #            expand=True,
                #            padding=ft.padding.all(15),
                #            content=ft.Column(
                #                controls=[
                #                    ft.Row(
                #                        controls=[
                #                            ft.Text(
                #                                value="Orders",
                #                                size=22,
                #                                color=Designer.colors[4]
                #                            ),
                #                        ]
                #                    ),
                #                    ft.Row(
                #                        controls=[
                #                            ft.Icon(
                #                                name=ft.icons.EDIT_DOCUMENT,
                #                                size=50,
                #                                color=Designer.colors[4],
                #                            ),
                #                            ft.Text(
                #                                value="You orders:",
                #                                size=22,
                #                                color=Designer.colors[4]
                #                            ),
                #                            ft.Text(
                #                                value=user_data_class.count_orders,
                #                                size=22,
                #                                color=Designer.colors[4]
                #                            ),
                #                        ]    
                #                    ),
                #                ]
                #            )
                #        )
                #    ]
                #),
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
                                                value="You address:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                            self.address_text
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
                                                value="You E-mail:",
                                                size=22,
                                                color=Designer.colors[4]
                                            ),
                                            self.email_text
                                        ]    
                                    ),
                                ]
                            )
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        Button(text="Save", metod=self.go_to_save)
                    ]
                )
            ]
        )
    
    def go_to_search(self,e):
        self.page.go("/prof_entry")
    #def go_to_seting(self,e):
    #    self.page.go("/seting")
    def go_to_save(self,e):
        data = {"id" : str(user_data_class.id),
                "email" : str(self.email_text.value),
                "login" : str(self.name_text.value),
                "password" : str(self.new_password_text.value),
                "phone_number" : str(self.phone_number_text.value),
                "region" : str(self.address_text.value),
                "is_active" : True
                }
        
        r = requests.get("http://31.31.196.6:8000/ozito/check_user?login="+data["login"])
        check = r.json()
        
        if check["message"] == 'Данный пользователь существует.':
            pass
        else:
            temp = requests.put("http://31.31.196.6:8000/ozito/update_user?id="+data["id"]+
                            "&email="+data["email"]+"&login="+data["login"]+"&password="+data["password"]+
                            "&phone_number="+data["phone_number"]+"&region="+data["region"]+"&is_active=true&role=user")
        

            user_data_class.name = data["login"]
            user_data_class.password = data["password"]
            user_data_class.phone_number = data["phone_number"]
            user_data_class.address = data["region"]
            user_data_class.email = data["email"]
        
            self.page.go("/prof_entry")