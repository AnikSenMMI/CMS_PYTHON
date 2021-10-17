import pathlib
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--start-fullscreen")
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        # self.driver.set_page_load_timeout(3000)
        # self.driver.get('https://ee-portal.augmedix.com/')
        self.driver.get('https://cms-dev.musiczi.com/')

    def tearDown(self):
        self.driver.close()
