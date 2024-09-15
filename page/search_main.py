import flet as ft
from disigner import ButtonIcon, Designer, ProductCard

class search_main():
    def __init__(self, page:ft.Page):
        self.page = page
        
        self.page_view = ft.View(
            bgcolor=Designer.colors[1],
            route="/search",
            controls=[
                ft.Row(
                    controls=[ft.Container(bgcolor="#000000",height=40, expand=True),]
                ),
                ft.Column(
                    expand=True,
                    controls=[
                        ProductCard(),
                        ProductCard(),
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
                        ft.IconButton(icon=ft.icons.SEARCH_OUTLINED, icon_size=50, icon_color=Designer.colors[4]),
                        ft.IconButton(icon=ft.icons.VIEW_COMPACT_ALT_OUTLINED, icon_size=50, icon_color=Designer.colors[4]),
                        ft.IconButton(icon=ft.icons.MESSENGER, icon_size=50, icon_color=Designer.colors[4]),
                        ft.IconButton(icon=ft.icons.ACCOUNT_BOX_ROUNDED, icon_size=50, icon_color=Designer.colors[4]),
                    ]
                ),
            ]
        )