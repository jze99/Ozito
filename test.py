import flet as ft
import requests
def main(page: ft.Page):
    
    temp = requests.get("http://31.31.196.6:8000/ozito/get_image?file_name=1.png")
    
    page.add(
        ft.Container(
            height=100,
            width=100,
            image=ft.DecorationImage(src="http://31.31.196.6:8000/ozito/get_image?file_name=1.png")
        )
    )

ft.app(main)