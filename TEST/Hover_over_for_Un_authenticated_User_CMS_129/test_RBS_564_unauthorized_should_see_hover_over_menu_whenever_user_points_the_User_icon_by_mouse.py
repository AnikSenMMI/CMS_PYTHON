from pages.signin_page import SignInPage
from pages.navigation_page import NavigationPage
from TEST.base_test import BaseTest
import time

class HoverOver(BaseTest):
    def test_RBS_564_unauthorized_should_see_hover_over_menu_whenever_user_points_the_User_icon_by_mouse(self):
        navigation = NavigationPage(self.driver)
        time.sleep(10)
        navigation.hover_over_user_icon()
        navigation.assert_user_account_hover_display_two_menus()



# python3 -m unittest TEST.test1
# python3 -m pytest -s TEST/test_functionality_group_posting.py --alluredir=ReportAllure &&  allure serve ReportAllure/
