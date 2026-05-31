class LoginPage:

    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client/#/auth/login')



    def login(self):
        self.page.get_by_placeholder("email@example.com").fill("test@atest.com")
        self.page.get_by_placeholder("enter your passsword").fill("Mponline@123")
        self.page.get_by_role("button", name="login").click()

