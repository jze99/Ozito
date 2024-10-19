import flet as ft
from typing import Callable, Any


class Designer():
    colors=[
            "#881766",
            "#C4C4C4",
            "#CBC5BF",
            "#F3F4F4",
            "#000000",
            "#FFFFFF",
        ]
    
class TextField(ft.TextField):
    def __init__(self, password:bool=False, can_reveal_password:bool=False, value:str=""):
        super().__init__(
            #adaptive=True,
            #dense=True,
            value=value,
            text_size=18,
            password=password,
            can_reveal_password=can_reveal_password,
            width=180,
            #height=35,
            cursor_color=Designer.colors[4],
            border_color=Designer.colors[4],
            color=Designer.colors[4],
            #text_size=20,
            #cursor_height = 18,
            #fill_color=Designer.colors[4],
            #focused_color=Designer.colors[4]
        )
class TextField2(ft.TextField):
    def __init__(self, password:bool=False, can_reveal_password:bool=False, value:str=""):
        super().__init__(
            adaptive=True,
            dense=True,
            value=value,
            expand=True,
            text_size=18,
            password=password,
            can_reveal_password=can_reveal_password,
            #width=180,
            #height=35,
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
            
class ButtonBox(ft.FilledTonalButton):
    def __init__(self, metod=None, text:str=None):
        if metod == None:
            super().__init__(
                height=39,
                width=156,
                text=text,
                style=ft.ButtonStyle(
                    bgcolor=Designer.colors[0],
                    shape=ft.RoundedRectangleBorder(radius=10),
                    color=Designer.colors[4],
                    text_style=ft.TextStyle(
                        size=20,
                    )
                )
            )
        else:
            super().__init__(
                on_click=metod,
                height=39,
                width=156,
                text=text,
                style=ft.ButtonStyle(
                    bgcolor=Designer.colors[0],
                    shape=ft.RoundedRectangleBorder(radius=10),
                    color=Designer.colors[4],
                    text_style=ft.TextStyle(
                        size=20,
                    )
                )
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
    def __init__(self, p_id : int, title:str="title", price:str="price", desc : str = "desc"):
        self.p_id = p_id
        self.title = title
        self.price = price
        self.desc = desc
        super().__init__(
            on_click=self.go_to_product_card,
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
        
    def go_to_product_card(self,e):
        from page.product_card import product_card
        
        product_card.name_page = self.title
        product_card.price_page = self.price
        product_card.Description_page = self.desc
        self.page.go("/product")
        
class SearchRow(ft.Container):
    def __init__(self, on_click_method : Callable[[Any], None]):
        
        self.text_field = ft.TextField(
                        border=ft.InputBorder.NONE,
                        expand=True,    
                        cursor_color=Designer.colors[4],
                        border_color=Designer.colors[4],
                        color=Designer.colors[4],
                        adaptive=True,
                        text_size=24,
                    )
        
        super().__init__(
            height=55,
            expand=True,
            border=ft.border.all(2,Designer.colors[4]),
            border_radius=ft.border_radius.all(10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        hover_color=Designer.colors[0],
                        icon=ft.icons.SEARCH_OUTLINED,
                        icon_size=40,
                        icon_color=Designer.colors[4],
                        on_click=on_click_method
                    ),
                    self.text_field                    
                ]
            )
        )
    
    def return_text_field(self):
        return self.text_field.value

class OrderRow(ft.Row):
    
    def __init__(self, p_id : int = 0, p_name : str = "", p_desc : str = "", p_price : int = 0, c_id : int = 0, p_category : str = "",
                 p_status : str = ""):
        self.p_id = p_id
        self.p_name = p_name
        self.p_desc = p_desc
        self.p_price = p_price
        self.c_id = c_id
        self.p_category = p_category
        self.p_status = p_status
        super().__init__(
            controls=[
                ft.Container(
                    on_click=self.go_to_order,
                    expand=True,
                    bgcolor=Designer.colors[3],
                    border_radius=ft.border_radius.all(10),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                height=100,
                                width=100,
                                bgcolor=Designer.colors[0],
                                margin=ft.margin.all(10),
                                border_radius=ft.border_radius.all(10)
                            ),
                            ft.Container(
                                expand=True,
                                #bgcolor=Designer.colors[4],
                                alignment=ft.alignment.center,
                                content=ft.Text(
                                    value=self.p_name,
                                    size=22,
                                    color=Designer.colors[4]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    
    def go_to_order(self,e):
        from page.order_page import order_page
        order_page.p_id = self.p_id
        order_page.name_page = self.p_name
        order_page.Description_page = self.p_desc
        order_page.price_page = self.p_price
        order_page.c_id = self.c_id
        order_page.Categorial_page = self.p_category
        order_page.status_page = self.p_status
        self.page.go("/order")
        
class massege_row(ft.Row):
    def __init__(self, ):
        super().__init__(
            controls=[
                ft.Container(
                    bgcolor=Designer.colors[4],
                    height=40,
                )
            ]
        )     
        
class dialog(ft.AlertDialog):
    def __init__(self,text:str=""):
        super().__init__(
            title=ft.Text(text),
        )   