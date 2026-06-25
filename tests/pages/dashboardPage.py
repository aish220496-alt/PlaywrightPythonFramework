class DashboardPage:


    def __init__(self, page):
        self.page = page

    def selectItems(self):
        self.page.locator(".card-body").filter(
            has_text="ZARA COAT 3"
        ).get_by_role("button", name="Add To Cart").click()

    def placeOrder(self):
        self.page.locator("[routerlink*='cart']").click()
        
        self.page.get_by_role("button", name="Buy Now").click()
         #self.page.locator(".btn btn-primary").click()





