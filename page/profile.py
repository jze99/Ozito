import flet as ft
from designer import Designer

class profile():
    def __init__(self, page:ft.Page):
        self.page = page
        self.number_user="123123123"
        self.ocen = "2.3"
        self.page_view=ft.Column(
            controls=[
                ft.Row( #top row
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center_left,
                            expand=True,
                            #bgcolor="#000000",
                            content=ft.IconButton(hover_color=Designer.colors[0],icon=ft.icons.ARROW_BACK_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            #bgcolor="#FF0000",
                            content=ft.Text(value="Account",size=26, color=Designer.colors[4])
                        ),
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            #bgcolor="#1529DD",
                            content=ft.IconButton(hover_color=Designer.colors[0],icon=ft.icons.SETTINGS_ROUNDED,icon_size=35, icon_color=Designer.colors[4])
                        ),
                    ]
                ),
                ft.Row(#prof data
                    controls=[
                        ft.Container(
                            bgcolor=Designer.colors[3],
                            expand=True,
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.CircleAvatar(
                                                content=ft.Icon(ft.icons.ABC),
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="name",
                                                color=Designer.colors[4],
                                                size=22,
                                            )
                                        ]    
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="role",
                                                color=Designer.colors[4],
                                                size=22,
                                            )
                                        ]    
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Account number:",
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            ft.Text(
                                                value=self.number_user,
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value=self.ocen,
                                                color=Designer.colors[4],
                                                size=22,
                                            ),
                                            ft.Icon(
                                                name=ft.icons.STAR_ROUNDED,
                                                size=30,
                                                color=Designer.colors[0]
                                            )
                                        ]
                                    ),
                                ]    
                            ),
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            bgcolor=Designer.colors[3],
                            expand=True,
                            padding=ft.padding.all(15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Orders",
                                                size=22,
                                                color=Designer.colors[4]
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    ]
                ),
            ]
        )