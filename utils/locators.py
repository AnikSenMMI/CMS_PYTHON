from selenium.webdriver.common.by import By


class UserIcon(object):
    user_icon = (By.XPATH, "//div[@class='dropbtn']")
    user_icon_menus = (By.XPATH, "//div[@class='dropdown-content']//span")
    create_an_account_menu = (By.XPATH, "//span[normalize-space()='Create An Account']//*[name()='svg']")


class SignInPageLocator(object):
    email = (By.XPATH, '//*[@id="email"]')
    password = (By.XPATH, '//*[@id="pass"]')
    signInBtn = (By.XPATH, '//button[@data-testid="royal_login_button"]')


class NavigationLocator(object):
    pass
