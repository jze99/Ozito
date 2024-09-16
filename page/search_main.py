import flet as ft
from designer import ButtonIcon, Designer, ProductCard,SearchRow

class search_main():
    def __init__(self, page:ft.Page):
        self.page = page
        
        self.page_view = ft.View(
            bgcolor=Designer.colors[1],
            route="/search",
            controls=[
                ft.Row(
                    controls=[SearchRow()]
                ),
                ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            expand=True,
                            scroll=ft.ScrollMode.ADAPTIVE,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                                ProductCard(),
                            ]
                        ),
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
        
    def go_to_profile(self,e):
        self.page.go("/prof_entry")