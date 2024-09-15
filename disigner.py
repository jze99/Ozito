import flet as ft

class Designer():
    colors=[
            "#EF8A17",
            "#C4C4C4",
            "#CBC5BF",
            "#F3F4F4",
            "#000000",
        ]
    
class TextField(ft.TextField):
    def __init__(self, password:bool=False, can_reveal_password:bool=False):
        super().__init__(
            adaptive=True,
            dense=True,
            password=password,
            can_reveal_password=can_reveal_password,
            width=180,
            height=35,
            cursor_color=Designer.colors[4],
            border_color=Designer.colors[4],
            color=Designer.colors[4],
            #text_size=20,
            #cursor_height = 18,
            #fill_color=Designer.colors[4],
            #focused_color=Designer.colors[4]
        )
        

class Button(ft.FilledTonalButton):
    def __init__(self, metod=None, text:str=None):
        if metod == None:
            super().__init__(
                height=39,
                width=180,
                text=text,
                style=ft.ButtonStyle(bgcolor=Designer.colors[0])
            )
        else:
            super().__init__(
                height=39,
                width=180,
                on_click=metod,
                text=text,
                style=ft.ButtonStyle(bgcolor=Designer.colors[0])
            )

class ButtonIcon(ft.Container):
    def __init__(self, icon:ft.icons, size:int):
        super().__init__(
            content=ft.Icon(
                name=icon
            ),
            width=size,
            height=size,  
        )
        
class ProductCard(ft.Container):
    def __init__(self, title:str="title", price:str="price"):
        super().__init__(
            bgcolor=Designer.colors[3],
            content=ft.Column(
                height=232,
                width=182,
                spacing=1,
                controls=[
                    ft.Row(
                        height=5
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                bgcolor="#923232",
                                height=160,
                                width=170,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[ft.Container(width=5), ft.Text(value=title, color="#000000", size=22)]
                    ),
                    ft.Row(
                        controls=[ft.Container(width=5), ft.Text(value=price, color="#000000", size=22)]
                    ),
                ]
            )
        )