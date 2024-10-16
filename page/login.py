import flet as ft
from designer import TextField, Designer, Button
import requests
import json
from user_data import user_data_class
class Login:
    
    def __init__(self, page):
        self.page=page
        self.login_text = TextField()
        self.password_text = TextField(password=True, can_reveal_password=True)
        self.page_view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ADAPTIVE,
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
                            value="Log in",
                            color="#000000"
                        )
                    ]
                ),
                ft.Row(
                    width=180,
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
                        ft.Text(
                            size=24,
                            value="Login",
                            color=Designer.colors[4]
                        )
                    ]
                ),
                ft.Row(# login field
                    width=180,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.login_text
                    ]
                ),
                ft.Row(# pass text
                    width=180,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Text(
                            size=24,
                            value="Password",
                            color=Designer.colors[4]
                        )
                    ]
                ),
                ft.Row(# pass field
                    width=180,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.password_text
                    ]
                ),
                ft.Row(
                    height=50,
                ),
                ft.Row(
                    width=180,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        Button(text="Log in", metod=self.go_to_etry)
                    ]
                ),
                ft.Row(
                    width=180,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        Button(text="Registration", metod=self.go_to_register)
                    ]
                )
            ]
        )
    
    def go_to_etry(self, e):
        log_temp=str(self.login_text.value)
        pass_temp=str(self.password_text.value)
        temp = requests.get("http://31.31.196.6:8000/ozito/check_user?login="+log_temp)
        if temp.status_code != 200:
            return
        tepm_js = json.loads(temp.content)
        if tepm_js["message"] == 'Данный пользователь существует.':
            if tepm_js["data"][0]["password"] == pass_temp:
                user_data_class.id = tepm_js['data'][0]["id"]
                user_data_class.name = tepm_js['data'][0]['login']
                user_data_class.role = tepm_js['data'][0]['role']
                user_data_class.password = tepm_js['data'][0]['password']
                user_data_class.phone_number = tepm_js['data'][0]['phone_number']
                user_data_class.address = tepm_js['data'][0]['region']
                user_data_class.email = tepm_js['data'][0]['email']
                user_data_class.rating = tepm_js['data'][0]['rating']
                self.page.go("/search")
            else:
                pass
        else:
            pass

    def go_to_register(self,e):
        self.page.go("/reg")