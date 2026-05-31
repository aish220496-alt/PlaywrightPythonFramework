from tests.pages.dashboardPage import DashboardPage
from tests.pages.loginPage import LoginPage


def test_e2e_webpage(page):
    loginpage = LoginPage(page)

    loginpage.navigate()
    loginpage.login()

    dashpage = DashboardPage(page)
    dashpage.selectItems()