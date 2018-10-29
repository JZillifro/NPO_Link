from sys import platform
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AcceptanceTests (TestCase):

    def setUp(self):
        self.homeurl = 'http://npolink.me/'
        if platform == "linux" or platform == "linux2":
            self.browser = webdriver.Chrome('./chrome_drivers/chromedriver_linux')
        elif platform == "darwin": # macOS
            self.browser =webdriver.Chrome('./chrome_drivers/chromedriver_macosx')
        elif platform == "win32":
            self.browser =webdriver.Chrome('./chrome_drivers/chromedriver.exe')
        self.browser.get(self.homeurl)

    # Tests that the browser title for the homepage is correct
    def test1(self):
        self.browser.get(self.homeurl)
        self.assertIn('NPOLink', self.browser.title)

    # Tests that the home page component on navigation bar works
    def test2(self):
        try:
            self.browser.find_element_by_link_text('Home').click()
            self.assertEqual("http://npolink.me/", self.browser.current_url)
        except NoSuchElementException:
            self.fail("The element doesn't exist")

    # Tests that the homepage header is correct
    def test3(self):
        self.browser.find_element_by_link_text('Home').click()
        given = self.browser.find_element_by_class_name("container").text
        self.assertIn('Welcome to NPOLink!', given)

    # Tests that nonprofits component on navigation bar works
    def test4(self):
        try:
            self.browser.find_element_by_link_text('Non-profits').click()
            self.assertEqual("http://npolink.me/nonprofits", self.browser.current_url)
        except NoSuchElementException:
            self.fail("The element doesn't exist")

    # Tests that the nonprofits header is correct
    def test5(self):
        self.browser.find_element_by_link_text('Non-profits').click()
        given = self.browser.find_element_by_class_name("container").text
        self.assertIn('Non-Profit Organizations', given)

    # Tests that categories component on navigation bar works
    def test6(self):
        try:
            self.browser.find_element_by_link_text('Categories').click()
            self.assertEqual("http://npolink.me/categories", self.browser.current_url)
        except NoSuchElementException:
            self.fail("The element doesn't exist")

    # Tests that the categories header is correct
    def test7(self):
        self.browser.find_element_by_link_text('Categories').click()
        given = self.browser.find_element_by_class_name("container").text
        self.assertIn('Categories', given)

    # Tests that locations component on navigation bar works
    def test8(self):
        try:
            self.browser.find_element_by_link_text('Locations').click()
            self.assertEqual("http://npolink.me/locations", self.browser.current_url)
        except NoSuchElementException:
            self.fail("The element doesn't exist")

    # Tests that the locations header is correct
    def test9(self):
        self.browser.find_element_by_link_text('Locations').click()
        given = self.browser.find_element_by_class_name("container").text
        self.assertIn('Locations', given)

    # Tests that about component on navigation bar works
    def test10(self):
        try:
            self.browser.find_element_by_link_text('About').click()
            self.assertEqual("http://npolink.me/about", self.browser.current_url)
        except NoSuchElementException:
            self.fail("The element doesn't exist")

    # Tests that the about header is correct
    def test11(self):
        self.browser.find_element_by_link_text('About').click()
        given = self.browser.find_element_by_class_name("container").text
        self.assertIn('About', given)

    # Tests that link to gitlab repository works
    def test12(self):
        self.browser.find_element_by_link_text('About').click()
        try:
            self.browser.find_element_by_link_text('GitLab Repository').click()
            self.assertEqual("https://gitlab.com/gerardomares/npolink", self.browser.current_url)
        except NoSuchElementException:
            self.fail("The element doesn't exist")

    def endBrowser(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
