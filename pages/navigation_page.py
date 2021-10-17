from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from time import sleep
from utils.openpyxlfunction import *


class NavigationPage(BasePage):
    def __init__(self, driver):
        self.user_icon_locator = locators.UserIcon
        self.data = testcase_data.Data
        super(NavigationPage, self).__init__(driver)

    def hover_over_user_icon(self):
        self.hover(*self.user_icon_locator.user_icon)
        sleep(5)

    def assert_user_account_hover_display_two_menus(self):
        elements = self.find_elements(*self.user_icon_locator.user_icon_menus)
        total_element = len(elements)
        print(total_element)
        assert total_element == 2

    def assert_user_account_should_contain_login_and_create_an_account_options(self):
        self.assert_user_account_hover_display_two_menus()
        elements = self.find_elements(*self.user_icon_locator.user_icon_menus)
        menu = []
        for element in elements:
            menu.append(element.text)

        print(menu)
        print(self.data.hover_over_menu)
        assert menu == self.data.hover_over_menu

    def hover_on_create_an_account_menu(self):
        self.hover(*self.user_icon_locator.create_an_account_menu)

    def assert_create_an_account_has_three_menus(self):
        elements = self.find_elements(*self.user_icon_locator.user_icon_menus)
        total_element = len(elements)
        print(total_element)
        assert total_element == 5
