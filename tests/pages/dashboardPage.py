class DashboardPage:


    def __init__(self, page):
        self.page = page

    def selectItems(self):
        self.page.locator(".card-body").filter(
            has_text="ZARA COAT 3"
        ).get_by_role("button", name="Add To Cart").click()





