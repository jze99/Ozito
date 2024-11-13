import flet as ft
from designer import TextField, Designer, Button, dialog
import requests
import json
from user_data import user_data_class as udc

class Registration:
    
    def __init__(self, page):
        self.page=page
        self.login_text = TextField()
        self.email_text = TextField()
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
                                value="Login",
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
                ft.Row(# email text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.Text(
                                size=18,
                                value="E-mail",
                                color=Designer.colors[4]
                            )
                        ),  
                    ]
                ),
                ft.Row(# email field
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.email_text
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
                                value="Confirm the password",
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
                        Button(text="Register", metod=self.go_to_etry)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        Button(text="Log in", metod=self.go_to_register)
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
        conpass_temp = str(self.conform_passw_text.value)
        phone_temp = str(self.phone_number_text.value)
        email_temp=str(self.email_text.value)
        region_temp=str(self.region_text.value)
        
        
        user_check = requests.get("http://31.31.196.6:8000/ozito/check_user?login="+log_temp)
        user_js = json.loads(user_check.content)
        
        if log_temp != "" and email_temp != "" and pass_temp != "" and phone_temp != "" and region_temp != "":
            if user_js['message'] == 'Данный пользователь не существует.':
                if phone_temp.isnumeric():
                    if conpass_temp == pass_temp: 
                        temp = requests.post("http://31.31.196.6:8000/ozito/create_user?email="+email_temp+
                                             "&login="+log_temp+"&password="+pass_temp+"&phone_number="+phone_temp+
                                             "&region="+region_temp+"&is_active=true&role=user")
                        
                        temp_js = json.loads(temp.content)
                        
                        udc.id = temp_js['task_id']['data']['id']
                        udc.name = temp_js['task_id']['data']['login']
                        udc.email = temp_js['task_id']['data']['email']
                        udc.role = temp_js['task_id']['data']['role']
                        udc.password = temp_js['task_id']['data']['password']
                        udc.phone_number = temp_js['task_id']['data']['phone_number']
                        udc.address = temp_js['task_id']['data']['region']
                        udc.rating = temp_js['task_id']['data']['rating']

                        self.page.go("/search")
                    else:
                        self.page.open(dialog(text="Confirm the password."))
                else:
                    self.page.open(dialog(text="Phone number must consist from digits."))
            else:
                self.page.open(dialog(text="Such user already exists."))
        else:
            self.page.open(dialog(text="All fields must be filled."))
        

    def go_to_register(self,e):
        self.page.go("/log")