from flet import View,Page, ScrollMode
from disigner import Designer
from page import login, registration, search_main

def ViewsHendler(page):
    log = login.Login(page=page).page_view
    reg = registration.Registration(page=page).page_view
    search = search_main.search_main(page=page)
    temp = search.page_view
    return{
        "/":View(
            route="/",
            controls=[
               
            ],
        ),
        "/log":View(
            route="/log",
            controls=[
                log
            ],
            bgcolor=Designer.colors[1],
        ),
        "/reg":View(
            route="/reg",
            controls=[
                reg
            ],
            bgcolor=Designer.colors[1],
            scroll=ScrollMode.ADAPTIVE,
        ),
        "/search":temp
    }
    