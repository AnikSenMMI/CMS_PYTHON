from pages.signin_page import SignInPage
from pages.navigation_page import NavigationPage
from TEST.base_test import BaseTest
import time


class HoverOverUserIcon(BaseTest):
    def test_RBS_565_The_hover_over_menu_should_display_within_Log_in_and_Create_An_Account_option(self):
        navigation = NavigationPage(self.driver)

        time.sleep(10)
        navigation.hover_over_user_icon()
        navigation.hover_on_create_an_account_menu()
        navigation.assert_create_an_account_has_three_menus()

# python3 -m unittest TEST.test1
# python3 -m pytest -s TEST/test_functionality_group_posting.py --alluredir=ReportAllure &&  allure serve ReportAllure/
