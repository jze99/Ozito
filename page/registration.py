import flet as ft
from designer import TextField, Designer, Button
import requests
class Registration:
    
    def __init__(self, page):
        self.page=page
        self.login_text = TextField()
        self.password_text = TextField(password=True, can_reveal_password=True)
        self.conform_passw_text = TextField(password=True, can_reveal_password=True)
        self.phone_number_text = TextField()
        self.region_text = TextField()
        self.page_view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
            controls=[
                ft.Row(
                    height=50,
                    controls=[
                        ft.Container(
                            expand=1,
                            #bgcolor="#22DB3B"
                        )
                    ]
                ),
                ft.Row(# заголовок страницы
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            size=36,
                            value="Registration",
                            color="#000000"
                        )
                    ]
                ),
    
                ft.Row(
                    height=50,
                    controls=[
                        ft.Container(
                            expand=1,
                            #bgcolor="#22DB3B"
                        )
                    ]
                ),
                ft.Row(# login text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.Text(
                                size=18,
                                value="Name",
                                color=Designer.colors[4]
                            )
                        ),  
                    ]
                ),
                ft.Row(# login field
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.login_text
                    ]
                ),
                ft.Row(# password text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.Text(
                                size=18,
                                value="Password",
                                color=Designer.colors[4]
                            )
                        ),  
                    ]
                ),
                ft.Row(# pass field
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.password_text
                    ]
                ),
                ft.Row(# password_conform text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.Text(
                                size=16,
                                value="Conform the password",
                                color=Designer.colors[4]
                            )
                        ),  
                    ]
                ),
                ft.Row(# password_conform field
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.conform_passw_text
                    ]
                ),
                ft.Row(# phone_number text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.Text(
                                size=18,
                                value="Phone number",
                                color=Designer.colors[4]
                            )
                        ),  
                    ]
                ),
                ft.Row(# phone_number field
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.phone_number_text
                    ]
                ),
                ft.Row(# region text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.Text(
                                size=18,
                                value="Region",
                                color=Designer.colors[4]
                            )
                        ),  
                    ]
                ),
                ft.Row(# region field
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.region_text
                    ]
                ),
                ft.Row(
                    height=50,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        Button(text="Entry", metod=self.go_to_etry)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        Button(text="Authorization", metod=self.go_to_register)
                    ]
                ),
                ft.Row(
                    height=350,
                ),
            ]
        )
    
    def go_to_etry(self, e):
        log_temp=str(self.login_text.value)
        pass_temp=str(self.password_text.value)
        temp = requests.post("http://31.31.196.6:8000/tasks/create_user?email="+log_temp+"&login="+log_temp+"&password="+pass_temp)

    def go_to_register(self,e):
        self.page.go("/log")