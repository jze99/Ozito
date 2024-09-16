from flet import View,Page, ScrollMode
from designer import Designer
from page import login, profile_entry, registration, search_main, profile_no_entry, seting

def ViewsHendler(page):
    log = login.Login(page=page).page_view
    reg = registration.Registration(page=page).page_view
    search = search_main.search_main(page=page)
    search = search.page_view
    prof_entry = profile_entry.profile(page=page).page_view
    prof_no_entry = profile_no_entry.profile_no_entry(page=page).page_view
    seting_= seting.seting(page=page).page_view
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
        "/prof_entry":View(
            route="/prof_entry",
            controls=[
                prof_entry
            ],
            bgcolor=Designer.colors[2],
        ),
        "/prof_no_entry":View(
            route="/prof_no_entry",
            controls=[
                prof_no_entry
            ],
            bgcolor=Designer.colors[5],
        ),
        "/seting":View(
            route="/seting",
            controls=[
                seting_
            ],
            bgcolor=Designer.colors[2],
        ),
    }
    