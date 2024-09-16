from flet import View,Page, ScrollMode
from designer import Designer
from page import login, registration, search_main, profile

def ViewsHendler(page):
    log = login.Login(page=page).page_view
    reg = registration.Registration(page=page).page_view
    search = search_main.search_main(page=page)
    search = search.page_view
    prof = profile.profile(page=page).page_view
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
        "/search":search,
        "/prof":View(
            route="/prof",
            controls=[
                prof
            ],
            bgcolor=Designer.colors[2],
        ),
    }
    