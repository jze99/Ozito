import flet as ft
from designer import Designer,TextField, dialog, file_picer
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
        self.file_picer = file_picer(on_result=self.file_picer_result)
        self.images = ft.Container(
            height=200,
            width=200,
            border_radius=ft.border_radius.all(10),
            bgcolor=Designer.colors[0],
            image=ft.DecorationImage(src=f"http://31.31.196.6:8000/ozito/get_image?file_name={self.c_id}{self.p_id}.png"),
            #on_click=lambda _: self.file_picer.pick_files(
            #    allowed_extensions=["png", "csv", "jpg", "jpeg"],
            #    file_type=ft.FilePickerFileType.CUSTOM,
            #    allow_multiple=False,
            #),
        )
        self.page.overlay.append(self.file_picer)
        self.path_images:str=""
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
                                self.images,
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
            self.page.open(dialog(text="Order can't be deleted since it was already bought."))
        
    def save_product(self, e):
        if self.status_order ==  "Выставлен":
            if self.name_order.value != "" and self.price_order.value != "" and self.Categorial_order.value != "" and self.Description_order.value != "":
                temp_price = str(self.price_order.value)
                if temp_price.isnumeric():
                    #self.load_images()
                    r = requests.put("http://31.31.196.6:8000/ozito/update_product?id="+str(self.p_id)+
                            "&product_name="+self.name_order.value+"&product_description="+
                            self.Description_order.value+"&price="+str(self.price_order.value)+"&creator_id="+str(self.c_id)
                            +"&status=%D0%92%D1%8B%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD&category="+self.Categorial_order.value)
                    self.page.go("/my_orders")
                else:
                    self.page.open(dialog(text="Price must consist of digits."))
            else:
                self.page.open(dialog(text="All fields must be filled."))
        else:
            self.page.open(dialog(text="Order can't be updated since it was already bought."))
    
    def file_picer_result(self,e):
        if e.files:
            self.path_images = e.files[0].path
            self.images.image = ft.DecorationImage(src=e.files[0].path)
            self.images.update()
    
    def load_images(self):
        from ftplib import FTP
        # Укажите ваши данные для подключения
        ftp_host = '31.31.196.6'  # адрес FTP-сервера
        ftp_user = 'u2806602'     # ваше имя пользователя
        ftp_pass = 'wE8aC4bF4uiZ7vL8'      # ваш пароль
        # Путь, куда вы хотите загрузить изображение на сервере
        remote_image_path = 'www/ozito.ru/images/'
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)

        # Открываем файл и загружаем его на сервер
        with open(self.path_images, 'rb') as image_file:
            ftp.storbinary('STOR ' + f"{remote_image_path}{self.c_id}{self.p_id}.png", image_file)  # Замените 'картинка.jpg' на нужное имя файла на сервере

        # Закрываем соединение
        ftp.quit()
    
    def go_to_orders(self,e):
        self.page.go("/my_orders")