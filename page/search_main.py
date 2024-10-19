import flet as ft
from designer import ButtonIcon, Designer, ProductCard,SearchRow
import requests
import json
from user_data import user_data_class as udc

class search_main():
    def __init__(self, page:ft.Page):
        self.page = page
        self.search = SearchRow(on_click_method=self.update_pages)
        self.temp=[]
        self.column_shop=ft.Column(
                            expand=True,
                            scroll=ft.ScrollMode.ADAPTIVE,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=self.load_prods()
                        )
        
        self.page_view = ft.View(
            bgcolor=Designer.colors[1],
            route="/search",
            controls=[
                ft.Row(
                    controls=[self.search]
                ),
                ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        self.column_shop
                    ]
                ),
                #ft.GridView(
                #    expand=True,
                #    #horizontal=True,
                #    #child_aspect_ratio=12,
                #    #max_extent=,
                #    clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
                #    runs_count=4,
                #    padding=ft.padding.all(10),
                #    controls=[
                #        
                #    ]
                #),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(hover_color=Designer.colors[0], icon=ft.icons.SEARCH_OUTLINED, icon_size=45, icon_color=Designer.colors[4]),
                        ft.IconButton(hover_color=Designer.colors[0], icon=ft.icons.VIEW_COMPACT_ALT_OUTLINED, icon_size=50, icon_color=Designer.colors[4]),
                        ft.IconButton(hover_color=Designer.colors[0], icon=ft.icons.MESSENGER_OUTLINE_ROUNDED, icon_size=45, icon_color=Designer.colors[4]),
                        ft.IconButton(on_click=self.go_to_profile,hover_color=Designer.colors[0], icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED, icon_size=45, icon_color=Designer.colors[4]),
                    ]
                ),
            ]
        )
    def load_prods(self):
        r = requests.get("http://31.31.196.6:8000/ozito/select_all_products")
        prod_js = json.loads(r.content)
        prods = []
        temp = self.search.return_text_field()
        for p in prod_js["data"]:
            if p["status"] == "Выставлен" and p["creator_id"] != udc.id:
                if temp == "":
                    prods.append(ProductCard(p["product_id"], p["product_name"], p["price"], p["product_description"]))
                elif temp in p["product_name"]:
                    prods.append(ProductCard(p["product_id"], p["product_name"], p["price"], p["product_description"]))
        return prods
        
    def update_pages(self,e):
        self.column_shop.controls = self.load_prods()
        self.column_shop.update()
        
    def go_to_profile(self,e):
        self.page.go("/prof_entry")