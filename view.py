from flet import View,Page, ScrollMode
from designer import Designer
from page import massages_page,product_card,crate_order,order_page,login, profile_entry, registration, search_main, profile_no_entry, seting, my_orders



def ViewsHendler(page):
    log = login.Login(page=page).page_view
    reg = registration.Registration(page=page).page_view
    search = search_main.search_main(page=page)
    search = search.page_view
    prof_entry = profile_entry.profile(page=page).page_view
    prof_no_entry = profile_no_entry.profile_no_entry(page=page).page_view
    seting_= seting.seting(page=page).page_view
    my_orders_= my_orders.my_order(page=page).page_view
    order_page_view=order_page.order_page(page=page).page_view
    create_order_ = crate_order.create_order_page(page=page).page_view 
    product_card_=product_card.product_card(page=page).page_view
    massages_page_ = massages_page.massages_page(page=page).page_view
    
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
        "/my_orders":View(
            route="/my_orders",
            controls=[
                my_orders_
            ],
            bgcolor=Designer.colors[2],
        ),
        "/order":View(
            route="/order",
            controls=[
                order_page_view
            ],
            bgcolor=Designer.colors[2],
        ),
        "/new_order":View(
            route="/new_order",
            controls=[
                create_order_
            ],
            bgcolor=Designer.colors[2],
        ),
        "/product":View(
            route="/product",
            controls=[
                product_card_
            ],
            bgcolor=Designer.colors[2],
        ),
        "/masseges":View(
            route="/masseges",
            controls=[
                massages_page_
            ],
            bgcolor=Designer.colors[2],
        ),
    }
    