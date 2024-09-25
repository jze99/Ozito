from flet import Page, app, AppView
from view import ViewsHendler

def main(page: Page):

    def PageLoading(route):
        print(page.route)
        page.views.clear()
        page.views.append(ViewsHendler(page=page)[page.route])
        page.update()
    page.on_route_change = PageLoading
    print(page.on_route_change)
    page.go("/prof_no_entry")
    
app(target=main, assets_dir="assets")
